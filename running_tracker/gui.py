import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from .data_handler import DataHandler
from .visualization import Visualization
from .stats_engine import StatsEngine


class StatsWindow(tk.Toplevel):
    """Display statistics in a simple table."""

    def __init__(self, master, stats: dict):
        super().__init__(master)
        self.title("Statistics")
        self.resizable(False, False)
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        columns = ("metric", "value")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=len(stats))
        tree.heading("metric", text="Metric")
        tree.heading("value", text="Value")
        for metric, value in stats.items():
            tree.insert("", tk.END, values=(metric, value))
        tree.pack(fill=tk.BOTH, expand=True)

class RunningTrackerApp:
    def __init__(self, config=None):
        self.root = tk.Tk()
        self.root.title("Running Tracker")
        ttk.Style().theme_use("clam")
        self.data_handler = DataHandler()
        self.stats_engine = StatsEngine(self.data_handler)
        self.visualization = Visualization(self.data_handler)
        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.grid(sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Date (YYYY-MM-DD)").grid(column=0, row=0, sticky=tk.W, pady=5)
        self.date_entry = ttk.Entry(frame)
        self.date_entry.grid(column=1, row=0, sticky="ew", pady=5)

        ttk.Label(frame, text="Distance (km)").grid(column=0, row=1, sticky=tk.W, pady=5)
        self.distance_entry = ttk.Entry(frame)
        self.distance_entry.grid(column=1, row=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Time (HH:MM:SS)").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.time_entry = ttk.Entry(frame)
        self.time_entry.grid(column=1, row=2, sticky="ew", pady=5)

        ttk.Button(frame, text="Add Run", command=self.add_run).grid(column=0, row=3, columnspan=2, pady=10)
        ttk.Button(frame, text="Show Stats", command=self.show_stats).grid(column=0, row=4, columnspan=2, pady=5)
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
        if not stats:
            messagebox.showinfo("Stats", "No data available")
            return
        StatsWindow(self.root, stats)

    def show_graphs(self):
        self.visualization.show_plots()

    def run(self):
        self.root.mainloop()
