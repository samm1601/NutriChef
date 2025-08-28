$ErrorActionPreference = "Stop"

# Move to script directory
Set-Location -Path $PSScriptRoot

# Paths
$projectRoot = "$PSScriptRoot"
$frontendDir = Join-Path $projectRoot "NutriChef" | Join-Path -ChildPath "frontend"

# Ensure dependencies are installed
Write-Host "Installing dependencies from NutriChef/requirements.txt..."
python -m pip install -r (Join-Path $projectRoot "NutriChef" | Join-Path -ChildPath "requirements.txt") | Out-Null

# Start API server
Write-Host "Starting API server on http://127.0.0.1:8000 ..."
$apiJob = Start-Job -ScriptBlock {
    python -m uvicorn NutriChef.api:app --port 8000 --reload
}

# Start static server for frontend
Write-Host "Starting frontend server on http://127.0.0.1:5500 ..."
$frontendJob = Start-Job -ArgumentList $frontendDir -ScriptBlock {
    param($feDir)
    Set-Location $feDir
    python -m http.server 5500
}

# Wait for ports to be ready
function Test-PortReady {
    param([int]$Port)
    try {
        $client = New-Object Net.Sockets.TcpClient
        $iar = $client.BeginConnect("127.0.0.1", $Port, $null, $null)
        $wait = $iar.AsyncWaitHandle.WaitOne(1000, $false)
        if ($wait -and $client.Connected) { $client.Close(); return $true } else { $client.Close(); return $false }
    } catch { return $false }
}

Write-Host "Waiting for servers to become ready..."
for ($i = 0; $i -lt 30; $i++) {
    $apiReady = Test-PortReady -Port 8000
    $feReady = Test-PortReady -Port 5500
    if ($apiReady -and $feReady) { break }
    Start-Sleep -Seconds 1
}

if (!(Test-PortReady -Port 8000) -or !(Test-PortReady -Port 5500)) {
    Write-Host "Warning: One or both services may not have started yet."
}

# Save job info for stopping later
$state = @{ ApiJobId = $apiJob.Id; FrontendJobId = $frontendJob.Id }
$state | ConvertTo-Json | Set-Content -Path (Join-Path $projectRoot ".run_state.json")

# Open browser to GUI
Start-Process "http://127.0.0.1:5500/"

Write-Host "Servers started. Use .\stop.ps1 to stop them."

