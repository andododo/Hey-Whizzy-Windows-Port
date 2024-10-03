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

echo All processes started.
echo Press any key to terminate all processes.
pause > nul

REM Terminate the npm process
echo Terminating React processes...
for /f "tokens=2" %%a in ('tasklist /fi "imagename eq node.exe" /fo list ^| find "PID:"') do (
    taskkill /F /PID %%a
)

REM Close the terminal windows by their titles
echo Closing Python terminal windows...
taskkill /FI "WINDOWTITLE eq Whizzy Logs*" /F
taskkill /FI "WINDOWTITLE eq UI Logs*" /F

echo All processes have been terminated.
timeout /t 2 > nul