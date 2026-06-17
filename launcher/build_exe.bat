@echo off
echo Building PeakBlox Windows EXE...

REM Install PyInstaller if needed
pip install pyinstaller

REM Build single executable
pyinstaller --onefile --windowed --name PeakBlox peakblox_launcher.py

echo Build complete! Check dist/PeakBlox.exe
echo.
echo Tip: Run the website first with "npm start" in the main folder for full experience.
pause