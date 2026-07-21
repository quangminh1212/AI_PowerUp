# List subrepo folders with no README file
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot '..')
Set-Location $repoRoot

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

$empty = foreach ($e in $entries) {
    $d = Join-Path $repoRoot $e.path
    if ((Test-Path $d -PathType Container) -and -not (Get-ChildItem $d -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '(?i)^readme' })) {
        $e
    }
}

"Total entries: $($entries.Count)"
"Empty folders: $($empty.Count)"
$empty | ForEach-Object { "$($_.path) -> $($_.url)" } | Select-Object -First 50
