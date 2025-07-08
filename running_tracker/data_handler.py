import csv
from pathlib import Path

DATA_FILE = Path("runs.csv")

class DataHandler:
    def __init__(self, filename=DATA_FILE):
        self.filename = Path(filename)
        if not self.filename.exists():
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "distance", "time"])

    def add_run(self, date, distance, time_str):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date.isoformat(), distance, time_str])

    def get_runs(self):
        with open(self.filename, newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
