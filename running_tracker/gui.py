import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from .assets import load_logo_b64

from .data_handler import DataHandler
from .visualization import Visualization
from .stats_engine import StatsEngine


class RunsWindow(tk.Toplevel):
    """Display individual runs and allow removal."""

    def __init__(self, master, data_handler: DataHandler):
        super().__init__(master)
        self.title("Runs")
        self.resizable(False, False)
        self.data_handler = data_handler

        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        columns = ("date", "distance", "time")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title())
        self.tree.pack(fill=tk.BOTH, expand=True)

        ttk.Button(frame, text="Remove Selected", command=self._remove_selected).pack(pady=5)

        self._populate()

    def _populate(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        runs = self.data_handler.get_runs()
        for idx, run in enumerate(runs):
            self.tree.insert("", tk.END, iid=str(idx), values=(run["date"], run["distance"], run["time"]))

    def _remove_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Remove Run", "No run selected")
            return
        idx = int(sel[0])
        try:
            self.data_handler.remove_run(idx)
            self._populate()
        except Exception as e:
            messagebox.showerror("Error", str(e))


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
        self._setup_style()
        self.logo_image = tk.PhotoImage(data=load_logo_b64())
        self.root.iconphoto(False, self.logo_image)
        self.data_handler = DataHandler()
        self.stats_engine = StatsEngine(self.data_handler)
        self.visualization = Visualization(self.data_handler)
        self._build_ui()

    def _setup_style(self):
        style = ttk.Style()
        bg = "#e7f0fd"
        self.root.configure(background=bg)
        style.configure("App.TFrame", background=bg)
        style.configure("TLabel", background=bg, font=("Segoe UI", 11))
        style.configure(
            "Header.TLabel",
            background=bg,
            foreground="#2c3e50",
            font=("Segoe UI", 16, "bold"),
        )
        style.configure(
            "TButton",
            background="#4a90e2",
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=6,
        )
        style.map(
            "TButton",
            background=[("active", "#357ABD")],
            foreground=[("active", "white")],
        )
        style.configure("TEntry", padding=5)

    def _build_ui(self):
        frame = ttk.Frame(self.root, padding=20, style="App.TFrame")
        frame.grid(sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        header = ttk.Label(
            frame,
            text="Running Tracker",
            image=self.logo_image,
            compound="left",
            style="Header.TLabel",
        )
        header.grid(column=0, row=0, columnspan=2, pady=(0, 10))

        ttk.Label(frame, text="Date (YYYY-MM-DD)").grid(column=0, row=1, sticky=tk.W, pady=5)
        self.date_entry = ttk.Entry(frame)
        self.date_entry.grid(column=1, row=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Distance (km)").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.distance_entry = ttk.Entry(frame)
        self.distance_entry.grid(column=1, row=2, sticky="ew", pady=5)

        ttk.Label(frame, text="Time (HH:MM:SS)").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.time_entry = ttk.Entry(frame)
        self.time_entry.grid(column=1, row=3, sticky="ew", pady=5)

        ttk.Button(frame, text="Add Run", command=self.add_run).grid(column=0, row=4, columnspan=2, pady=10)
        ttk.Button(frame, text="Show Stats", command=self.show_stats).grid(column=0, row=5, columnspan=2, pady=5)
        ttk.Button(frame, text="Show Graphs", command=self.show_graphs).grid(column=0, row=6, columnspan=2)
        ttk.Button(frame, text="View Runs", command=self.show_runs).grid(column=0, row=7, columnspan=2, pady=5)

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

    def show_runs(self):
        RunsWindow(self.root, self.data_handler)

    def run(self):
        self.root.mainloop()
