# Running Tracker App

This is a simple desktop application for tracking your running sessions.
Runs are stored in a local CSV file and basic statistics and graphs are available.
The interface now sports a more colorful theme and a small built‑in logo so it
feels a bit more like a modern web app.

## Requirements
- Python 3
- Tkinter (usually included with Python)
- matplotlib

Install matplotlib with:
```bash
pip install matplotlib
```

## Usage
Run the application using:
```bash
python -m running_tracker.main
```

A window will appear where you can enter the date, distance in km and the time
for each run. Basic statistics now open in a separate window and are displayed
in a small table. You can also view a distance-over-time graph.

### macOS clickable launch script

If you are on macOS you can double‑click `run.command` to start the
application. Make sure the file is executable:

```bash
chmod +x run.command
```

### Building a standalone macOS app

To generate a `.app` bundle that you can open like any other macOS
application, run `build_mac.command`. It relies on [PyInstaller](https://pyinstaller.org/):

```bash
chmod +x build_mac.command
./build_mac.command
```

The built application will appear in the `dist/` directory as `RunningTracker.app`.
