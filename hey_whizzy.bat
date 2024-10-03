@echo off

REM Run the first Python script in a new window
start "Whizzy Logs" cmd /k python raspi\init.py

REM Run the second Python script in a new window
start "UI Logs" cmd /k python raspi\back_ui.py

setlocal enabledelayedexpansion

REM Store the current directory
set ORIGINAL_DIR=%CD%

REM Change to the React project directory
cd raspi\ui

REM Start the React project
start "React UI" cmd /c npm start

REM Return to the original directory
cd %ORIGINAL_DIR%

echo React project started.
echo Press any key to terminate the React project.
pause > nul

REM Terminate the npm process
for /f "tokens=2" %%a in ('tasklist /fi "imagename eq node.exe" /fo list ^| find "PID:"') do (
    taskkill /F /PID %%a
)

echo React project has been terminated.
timeout /t 2 > nul