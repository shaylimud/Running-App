import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from data_handler import DataHandler
from visualization import Visualization
from stats_engine import StatsEngine

class RunningTrackerApp:
    def __init__(self, config=None):
        self.root = tk.Tk()
        self.root.title("Running Tracker")
        self.data_handler = DataHandler()
        self.stats_engine = StatsEngine(self.data_handler)
        self.visualization = Visualization(self.data_handler)
        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        ttk.Label(frame, text="Date (YYYY-MM-DD)").grid(column=0, row=0, sticky=tk.W)
        self.date_entry = ttk.Entry(frame)
        self.date_entry.grid(column=1, row=0)

        ttk.Label(frame, text="Distance (km)").grid(column=0, row=1, sticky=tk.W)
        self.distance_entry = ttk.Entry(frame)
        self.distance_entry.grid(column=1, row=1)

        ttk.Label(frame, text="Time (HH:MM:SS)").grid(column=0, row=2, sticky=tk.W)
        self.time_entry = ttk.Entry(frame)
        self.time_entry.grid(column=1, row=2)

        ttk.Button(frame, text="Add Run", command=self.add_run).grid(column=0, row=3, columnspan=2)
        ttk.Button(frame, text="Show Stats", command=self.show_stats).grid(column=0, row=4, columnspan=2)
        ttk.Button(frame, text="Show Graphs", command=self.show_graphs).grid(column=0, row=5, columnspan=2)

    def add_run(self):
        try:
            date = datetime.strptime(self.date_entry.get(), "%Y-%m-%d").date()
            distance = float(self.distance_entry.get())
            time_str = self.time_entry.get()
            self.data_handler.add_run(date, distance, time_str)
            messagebox.showinfo("Success", "Run added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_stats(self):
        stats = self.stats_engine.compute_stats()
        messagebox.showinfo("Stats", stats)

    def show_graphs(self):
        self.visualization.show_plots()

    def run(self):
        self.root.mainloop()
