# Copy README files to duplicate-URL subrepo folders.
# For each URL that appears in multiple submodule paths, if at least one path
# already has a README, copy it (with its original filename) to all sibling
# paths that are empty.

$ErrorActionPreference = 'Stop'
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot '..')
Set-Location $repoRoot

# Parse .gitmodules
$entries = New-Object System.Collections.Generic.List[object]
$current = $null
foreach ($line in Get-Content (Join-Path $repoRoot '.gitmodules')) {
    if ($line -match '^\[submodule\s+"([^"]+)"\]') {
        if ($current) { $entries.Add($current) }
        $current = [pscustomobject]@{ name = $Matches[1]; path = $null; url = $null }
    }
    elseif ($line -match '^\s*path\s*=\s*(.+)\s*$' -and $current) { $current.path = $Matches[1].Trim() }
    elseif ($line -match '^\s*url\s*=\s*(.+)\s*$' -and $current) { $current.url = $Matches[1].Trim() }
}
if ($current) { $entries.Add($current) }

# Group by URL
$groups = $entries | Group-Object -Property url
$copyCount = 0; $emptyAfter = 0; $unique404 = 0

foreach ($g in $groups) {
    if ($g.Count -lt 2) { continue }  # only duplicates matter
    $paths = $g.Group | Select-Object -ExpandProperty path

    # Find source README
    $sourcePath = $null; $sourceFile = $null
    foreach ($p in $paths) {
        $dir = Join-Path $repoRoot $p
        if (Test-Path $dir) {
            $readme = Get-ChildItem $dir -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '(?i)^readme' } | Select-Object -First 1
            if ($readme) { $sourcePath = $p; $sourceFile = $readme.FullName; break }
        }
    }

    if (-not $sourceFile) { $unique404++; continue }

    foreach ($p in $paths) {
        if ($p -eq $sourcePath) { continue }
        $dir = Join-Path $repoRoot $p
        if (-not (Test-Path $dir)) { continue }
        $existing = Get-ChildItem $dir -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '(?i)^readme' }
        if ($existing) { continue }
        $destFile = Join-Path $dir ([System.IO.Path]::GetFileName($sourceFile))
        Copy-Item $sourceFile $destFile -Force
        $copyCount++
        Write-Host "Copied -> $p"
    }
}

# Recount empty folders
foreach ($e in $entries) {
    $dir = Join-Path $repoRoot $e.path
    if ((Test-Path $dir) -and -not (Get-ChildItem $dir -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '(?i)^readme' })) {
        $emptyAfter++
    }
}

Write-Host ""
Write-Host "Copied README to $copyCount duplicate folders."
Write-Host "URLs with all paths 404: $unique404"
Write-Host "Empty folders after copy: $emptyAfter"
