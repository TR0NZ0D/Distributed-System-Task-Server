@echo off
setlocal

set "directoryToCheck=node_modules"

if exist "%directoryToCheck%\" (
    echo "Dependencies already installed!"
) else (
    call npm install
)

echo:
call npm start

echo:
pause