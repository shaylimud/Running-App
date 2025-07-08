#!/bin/bash
# Build Running Tracker App for macOS using PyInstaller
cd "$(dirname "$0")"

# Install PyInstaller if needed
if ! command -v pyinstaller >/dev/null 2>&1; then
    pip3 install --user pyinstaller
fi

pyinstaller --windowed --name "RunningTracker" main.py

echo "App built at dist/RunningTracker.app"
