@echo off
cd /d "%~dp0backend"

echo Starting CyberNexus Dashboard...
echo.
echo Open your browser at:
echo http://127.0.0.1:8000/
echo.

python -m uvicorn main:app --reload

pause