# Uploads a built site to the webserver with WinSCP, from this machine instead of from a
# Github runner. Useful when the host is refusing connections from the runner: run the
# workflow with both "preview" and "dry_run" ticked, download the artifact, unpack it into
# _out\ and upload from here.
#
# Credentials stay in WinSCP: create a stored site there (Session -> Save) and pass its name.
# Nothing secret is stored in this script or in this repo.
#
# Usage:
#   .\deploy_local_winscp.ps1 -Site "geodms.nl"
#   .\deploy_local_winscp.ps1 -Site "geodms.nl" -SkipBuild
#   .\deploy_local_winscp.ps1 -Site "geodms.nl" -LocalDir _out\new -RemoteDir /public_html/new -SkipBuild
#
# Note: jekyll rewrites every output file on each build, so this uploads the whole site every
# time. The Github Actions deploy only transfers the files that changed.
param(
    [Parameter(Mandatory = $true)][string]$Site,
    [string]$LocalDir = "_out",
    [string]$RemoteDir = "/public_html",
    [switch]$SkipBuild
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not $SkipBuild) {
    python convert_wiki_to_static_html.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

if (-not (Test-Path $LocalDir)) {
    throw "$LocalDir does not exist. Build first, or unpack the workflow artifact into it."
}

$winscp = "C:\Program Files (x86)\WinSCP\WinSCP.com"
if (-not (Test-Path $winscp)) { $winscp = "C:\Program Files\WinSCP\WinSCP.com" }
if (-not (Test-Path $winscp)) { throw "WinSCP not found; install it or adjust the path in this script." }

& $winscp /command `
    "open ""$Site""" `
    "synchronize remote ""$LocalDir"" ""$RemoteDir""" `
    "exit"
exit $LASTEXITCODE
