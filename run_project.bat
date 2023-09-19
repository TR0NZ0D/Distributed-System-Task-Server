@echo off

if "%1" == "/goto" goto :%2

@REM ============== MAIN ==============
:Start
echo Starting servers...
echo:

echo starting reports server...
start cmd /c %0 /goto RunReportsServer
echo:
echo starting todo server...
start cmd /c %0 /goto RunTodoServer
echo:
echo starting client server...
start cmd /c %0 /goto RunClientServer

goto :End

@REM ============== REPORTS ==============
:RunReportsServer
echo Requesting reports server to start...
echo:
call %~dp0ReportsServer\run_reports_server.bat

goto :ReportsServerEnd

@REM ============== TODO ==============
:RunTodoServer
echo Requesting todo server to start...
echo:
cd %~dp0TodoServer\TodoList.Api
call run_todo_server.bat

goto :TodoServerEnd

@REM ============== CLIENT ==============
:RunClientServer
echo Requesting client server to start...
echo:
call %~dp0Client\run_client_server.bat

goto :ClientServerEnd

@REM ============== END REPORTS ==============
:ReportsServerEnd
echo:
echo Reports server done.
echo Goodbye!
exit 0

@REM ============== END TODO ==============
:TodoServerEnd
echo:
echo Todo server done.
echo Goodbye!
exit 0

@REM ============== END CLIENT ==============
:ClientServerEnd
echo:
echo Client server done.
echo Goodbye!
exit 0

@REM ============== END MAIN ==============
:End
echo:
echo All servers initialization requested...
echo Goodbye!
exit 0
