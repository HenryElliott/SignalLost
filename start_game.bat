@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed or not in PATH.
    pause
    exit /b 1
)

REM Launch the game in a new PowerShell window and keep it open
powershell -NoExit -Command "python .\main.py"
