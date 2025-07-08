from statistics import mean

class StatsEngine:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def compute_stats(self):
        """Return basic statistics as a dictionary."""
        runs = self.data_handler.get_runs()
        if not runs:
            return {}

        distances = [float(r["distance"]) for r in runs]
        total_distance = sum(distances)
        avg_distance = mean(distances)

        return {
            "Total Runs": len(runs),
            "Total Distance (km)": f"{total_distance:.2f}",
            "Average Distance (km)": f"{avg_distance:.2f}",
        }
