@echo off

REM List of required libraries
set "LIBRARIES=pytube beautifulsoup4 requests"

REM Loop through each library and check if it's installed
for %%i in (%LIBRARIES%) do (
    python -c "import %%i" 2>nul
    if errorlevel 1 (
        echo Installing %%i...
        pip install %%i
    ) else (
        echo %%i is already installed.
    )
)

echo All required libraries have been checked and installed if needed.

pause

REM Delete the batch file
del %0
