@echo off
echo Building PeakBlox Windows EXE...

REM Install PyInstaller if needed
pip install pyinstaller

REM Build single executable
pyinstaller --onefile --windowed --icon=icon.ico --name PeakBlox peakblox_launcher.py

echo Build complete! Check dist/PeakBlox.exe
pause