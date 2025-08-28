$ErrorActionPreference = "SilentlyContinue"

Set-Location -Path $PSScriptRoot

$statePath = Join-Path $PSScriptRoot ".run_state.json"
if (Test-Path $statePath) {
    $state = Get-Content $statePath | ConvertFrom-Json
    if ($state.ApiJobId) { Stop-Job -Id $state.ApiJobId -Force | Out-Null; Receive-Job -Id $state.ApiJobId -Keep | Out-Null; Remove-Job -Id $state.ApiJobId -Force | Out-Null }
    if ($state.FrontendJobId) { Stop-Job -Id $state.FrontendJobId -Force | Out-Null; Receive-Job -Id $state.FrontendJobId -Keep | Out-Null; Remove-Job -Id $state.FrontendJobId -Force | Out-Null }
    Remove-Item $statePath -Force
}

# Also try killing typical processes if jobs were lost
Get-Process -Name "python" -ErrorAction SilentlyContinue | Where-Object { $_.Path -like "*Python*" } | ForEach-Object {
    if ($_.MainWindowTitle -like "*uvicorn*") { $_ | Stop-Process -Force }
}

Write-Host "Servers stopped."

