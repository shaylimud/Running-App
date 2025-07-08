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

    def remove_run(self, index: int):
        """Remove a run by its index in the CSV file."""
        runs = self.get_runs()
        if index < 0 or index >= len(runs):
            raise IndexError("Run index out of range")
        del runs[index]
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "distance", "time"])
            writer.writeheader()
            for row in runs:
                writer.writerow(row)
