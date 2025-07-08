import matplotlib.pyplot as plt
from datetime import datetime

class Visualization:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def show_plots(self):
        runs = self.data_handler.get_runs()
        if not runs:
            print("No data to plot")
            return
        dates = [datetime.fromisoformat(r["date"]) for r in runs]
        distances = [float(r["distance"]) for r in runs]
        plt.figure(figsize=(8,4))
        plt.plot(dates, distances, marker='o')
        plt.title("Distance Over Time")
        plt.xlabel("Date")
        plt.ylabel("Distance (km)")
        plt.tight_layout()
        plt.show()
