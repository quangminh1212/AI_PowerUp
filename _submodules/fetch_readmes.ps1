# Fetch README files for all submodules listed in .gitmodules
# Uses `gh api` (authenticated) to find the README regardless of file extension,
# then downloads it into the existing <category>/<subrepo>/ folder at repo root.
#
# Usage:
#   pwsh -File _submodules\fetch_readmes.ps1
#   pwsh -File _submodules\fetch_readmes.ps1 -DryRun     # only print plan, no downloads
#   pwsh -File _submodules\fetch_readmes.ps1 -Max 20     # cap for testing

[CmdletBinding()]
param(
    [switch]$DryRun,
    [int]$Max = 0,
    [string]$GitmodulesPath,
    [string]$RepoRoot
)

$ErrorActionPreference = 'Stop'
$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if (-not $GitmodulesPath) { $GitmodulesPath = (Resolve-Path (Join-Path (Join-Path $ScriptDir '..') '.gitmodules')).Path }
if (-not $RepoRoot)       { $RepoRoot       = (Resolve-Path (Join-Path $ScriptDir '..')).Path }
Set-Location $RepoRoot

# --- Parse .gitmodules --------------------------------------------------------
$entries = New-Object System.Collections.Generic.List[object]
$current = $null
foreach ($line in Get-Content $GitmodulesPath) {
    if ($line -match '^\[submodule\s+"([^"]+)"\]') {
        if ($current) { $entries.Add($current) }
        $current = [pscustomobject]@{ name = $Matches[1]; path = $null; url = $null }
    }
    elseif ($line -match '^\s*path\s*=\s*(.+)$' -and $current) {
        $current.path = $Matches[1].Trim()
    }
    elseif ($line -match '^\s*url\s*=\s*(.+)$' -and $current) {
        $current.url = $Matches[1].Trim()
    }
}
if ($current) { $entries.Add($current) }

Write-Host "Parsed $($entries.Count) submodule entries from $GitmodulesPath"

# --- Dedupe by URL (keep first occurrence) -----------------------------------
$seen = New-Object 'System.Collections.Generic.HashSet[string]'
$unique = New-Object System.Collections.Generic.List[object]
foreach ($e in $entries) {
    if (-not $e.url) { continue }
    if ($seen.Add($e.url)) { $unique.Add($e) }
}
Write-Host "Unique URLs: $($unique.Count) (skipped $($entries.Count - $unique.Count) duplicates)"

if ($Max -gt 0) { $unique = $unique.GetRange(0, [Math]::Min($Max, $unique.Count)) }

# --- Helper: parse owner/repo from git URL -----------------------------------
function Get-OwnerRepo($url) {
    # https://github.com/OWNER/REPO.git  or  git@github.com:OWNER/REPO.git
    if ($url -match 'github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?(?:/|$)') {
        return @($Matches[1], $Matches[2])
    }
    return $null
}

# --- Main fetch loop ----------------------------------------------------------
$ok = 0; $missing = 0; $errors = 0
$missingLog = Join-Path $PSScriptRoot 'fetch_readmes.missing.txt'
$errorLog   = Join-Path $PSScriptRoot 'fetch_readmes.errors.txt'
Remove-Item $missingLog, $errorLog -ErrorAction SilentlyContinue

$i = 0
foreach ($e in $unique) {
    $i++
    $or = Get-OwnerRepo $e.url
    if (-not $or) {
        $missing++
        "$($e.path)`t$($e.url)`tNOT_GITHUB" | Add-Content $missingLog
        continue
    }
    $owner, $repo = $or
    $destDir = Join-Path $RepoRoot $e.path
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    if ($DryRun) {
        Write-Host ("[{0}/{1}] DRY {2}/{3} -> {4}" -f $i, $unique.Count, $owner, $repo, $e.path)
        continue
    }

    try {
        # gh api repos/:owner/:repo/readme returns JSON with .name, .download_url, .content
        $json = gh api "repos/$owner/$repo/readme" 2>$null | Out-String
        if (-not $json.Trim()) {
            $missing++
            "$($e.path)`t$($e.url)`tNO_README" | Add-Content $missingLog
            Write-Host ("[{0}/{1}] MISS {2}/{3} (no README)" -f $i, $unique.Count, $owner, $repo) -ForegroundColor Yellow
            continue
        }
        $meta = $json | ConvertFrom-Json
        $readmeName = $meta.name
        $downloadUrl = $meta.download_url
        $destFile = Join-Path $destDir $readmeName

        if ($downloadUrl) {
            Invoke-WebRequest -Uri $downloadUrl -OutFile $destFile -UseBasicParsing
        } else {
            # Fallback: decode base64 content
            $content = $meta.content
            if (-not $content) { throw "no content and no download_url" }
            # Strip newlines that GitHub inserts in base64
            $clean = ($content -replace '\s', '')
            [System.IO.File]::WriteAllBytes($destFile, [Convert]::FromBase64String($clean))
        }
        $ok++
        Write-Host ("[{0}/{1}] OK   {2}/{3} -> {4}" -f $i, $unique.Count, $owner, $repo, (Join-Path $e.path $readmeName)) -ForegroundColor Green
    }
    catch {
        $errors++
        "$($e.path)`t$($e.url)`t$($_.Exception.Message)" | Add-Content $errorLog
        Write-Host ("[{0}/{1}] ERR  {2}/{3}: {4}" -f $i, $unique.Count, $owner, $repo, $_.Exception.Message) -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Done. OK=$ok  MISSING=$missing  ERRORS=$errors  TOTAL=$($unique.Count)"
if (Test-Path $missingLog) { Write-Host "Missing log: $missingLog" }
if (Test-Path $errorLog)   { Write-Host "Error log:   $errorLog" }
