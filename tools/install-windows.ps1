# Installs the base programs the video editor needs on Windows.
# Claude runs this during /setup-tools. You can also run it yourself:
#   Right-click Start > Terminal, then:
#   powershell -ExecutionPolicy Bypass -File tools\install-windows.ps1
#
# Safe to run more than once: winget skips anything already installed.

$ErrorActionPreference = "Continue"

function Install-App($id, $name) {
    Write-Host "`n=== $name ===" -ForegroundColor Cyan
    winget install --id $id -e --accept-source-agreements --accept-package-agreements --silent
}

Install-App "Git.Git"              "Git (saves your setup to GitHub)"
Install-App "OpenJS.NodeJS.LTS"    "Node.js (runs Remotion and HyperFrames)"
Install-App "Python.Python.3.12"   "Python (runs Whisper)"
Install-App "Gyan.FFmpeg"          "FFmpeg (cuts and exports video)"
Install-App "yt-dlp.yt-dlp"        "yt-dlp (downloads reference videos)"

Write-Host "`nAll installs attempted." -ForegroundColor Green
Write-Host "IMPORTANT: close this window and open a NEW terminal so Windows can find the new programs." -ForegroundColor Yellow
Write-Host "Then run:  python -m pip install faster-whisper `"av<19`""
