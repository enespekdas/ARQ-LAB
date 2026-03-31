@echo off
set PROMPT_TEXT=%~1
echo %PROMPT_TEXT% | findstr /I "Username" >nul
if %ERRORLEVEL%==0 (
  echo %ARQ_GIT_ASKPASS_USERNAME%
  exit /b 0
)
echo %ARQ_GIT_ASKPASS_PASSWORD%
