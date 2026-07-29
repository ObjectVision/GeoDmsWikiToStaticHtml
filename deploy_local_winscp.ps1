# Builds the site and uploads template\_site to the webserver with WinSCP.
# Credentials stay in WinSCP: create a stored site there (Session -> Save) and
# pass its name here. Nothing secret is stored in this script or repo.
#
# Usage:
#   .\deploy_local_winscp.ps1 -Site "geodms.nl"
#   .\deploy_local_winscp.ps1 -Site "geodms.nl" -RemoteDir /public_html -SkipBuild
#
# Note: jekyll rewrites every output file on each build, so this uploads the
# whole site every time. The Github Actions deploy only transfers changed files.
param(
    [Parameter(Mandatory = $true)][string]$Site,
    [string]$RemoteDir = "/public_html",
    [switch]$SkipBuild
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not $SkipBuild) {
    python convert_wiki_to_static_html.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

$winscp = "C:\Program Files (x86)\WinSCP\WinSCP.com"
if (-not (Test-Path $winscp)) { $winscp = "C:\Program Files\WinSCP\WinSCP.com" }

& $winscp /command `
    "open ""$Site""" `
    "synchronize remote ""template\_site"" ""$RemoteDir""" `
    "exit"
exit $LASTEXITCODE
