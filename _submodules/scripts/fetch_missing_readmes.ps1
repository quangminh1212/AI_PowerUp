# Fetch README files for submodules that don't have a README on disk yet.
# Uses `gh api` (authenticated). Skips folders that already contain any README* file.

[CmdletBinding()]
param(
    [switch]$DryRun,
    [int]$Max = 0
)

$ErrorActionPreference = 'Stop'
$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$RepoRoot = Resolve-Path (Join-Path (Join-Path $ScriptDir '..') '..')
Set-Location $RepoRoot

$GitmodulesPath = Join-Path $RepoRoot '.gitmodules'

# Parse .gitmodules
$entries = New-Object System.Collections.Generic.List[object]
$current = $null
foreach ($line in Get-Content $GitmodulesPath) {
    if ($line -match '^\[submodule\s+"([^"]+)"\]') {
        if ($current) { $entries.Add($current) }
        $current = [pscustomobject]@{ name = $Matches[1]; path = $null; url = $null }
    }
    elseif ($line -match '^\s*path\s*=\s*(.+?)\s*$' -and $current) { $current.path = $Matches[1].Trim() }
    elseif ($line -match '^\s*url\s*=\s*(.+?)\s*$' -and $current) { $current.url = $Matches[1].Trim() }
}
if ($current) { $entries.Add($current) }

# Filter to those missing README
$todo = New-Object System.Collections.Generic.List[object]
foreach ($e in $entries) {
    $dir = Join-Path $RepoRoot $e.path
    if (Test-Path $dir) {
        $hasReadme = Get-ChildItem $dir -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '(?i)^readme' }
        if (-not $hasReadme) { $todo.Add($e) }
    }
    else {
        $todo.Add($e)
    }
}

Write-Host "Submodules missing README: $($todo.Count)"
if ($Max -gt 0) { $todo = $todo.GetRange(0, [Math]::Min($Max, $todo.Count)) }

function Get-OwnerRepo($url) {
    if ($url -match 'github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?(?:/|$)') {
        return @($Matches[1], $Matches[2])
    }
    return $null
}

$ok = 0; $missing = 0; $errors = 0
$missingLog = Join-Path $ScriptDir 'fetch_missing.missing.txt'
$errorLog   = Join-Path $ScriptDir 'fetch_missing.errors.txt'
Remove-Item $missingLog, $errorLog -ErrorAction SilentlyContinue

$i = 0
foreach ($e in $todo) {
    $i++
    $or = Get-OwnerRepo $e.url
    if (-not $or) {
        $missing++
        "$($e.path)`t$($e.url)`tNOT_GITHUB" | Add-Content $missingLog
        continue
    }
    $owner, $repo = $or
    $destDir = Join-Path $RepoRoot $e.path
    if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }

    if ($DryRun) {
        Write-Host ("[{0}/{1}] DRY {2}/{3} -> {4}" -f $i, $todo.Count, $owner, $repo, $e.path)
        continue
    }

    try {
        $json = gh api "repos/$owner/$repo/readme" 2>$null | Out-String
        if (-not $json.Trim()) {
            $missing++
            "$($e.path)`t$($e.url)`tNO_README" | Add-Content $missingLog
            Write-Host ("[{0}/{1}] MISS {2}/{3}" -f $i, $todo.Count, $owner, $repo) -ForegroundColor Yellow
            continue
        }
        $meta = $json | ConvertFrom-Json
        $readmeName = $meta.name
        $downloadUrl = $meta.download_url
        $destFile = Join-Path $destDir $readmeName

        if ($downloadUrl) {
            Invoke-WebRequest -Uri $downloadUrl -OutFile $destFile -UseBasicParsing
        } else {
            $content = $meta.content
            if (-not $content) { throw "no content" }
            $clean = ($content -replace '\s', '')
            [System.IO.File]::WriteAllBytes($destFile, [Convert]::FromBase64String($clean))
        }
        $ok++
        Write-Host ("[{0}/{1}] OK   {2}/{3} -> {4}" -f $i, $todo.Count, $owner, $repo, (Join-Path $e.path $readmeName)) -ForegroundColor Green
    }
    catch {
        $errors++
        "$($e.path)`t$($e.url)`t$($_.Exception.Message)" | Add-Content $errorLog
        Write-Host ("[{0}/{1}] ERR  {2}/{3}: {4}" -f $i, $todo.Count, $owner, $repo, $_.Exception.Message) -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Done. OK=$ok  MISSING=$missing  ERRORS=$errors  TOTAL=$($todo.Count)"
if (Test-Path $missingLog) { Write-Host "Missing log: $missingLog" }
if (Test-Path $errorLog)   { Write-Host "Error log:   $errorLog" }
