from statistics import mean

class StatsEngine:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def compute_stats(self):
        runs = self.data_handler.get_runs()
        if not runs:
            return "No data available"
        distances = [float(r["distance"]) for r in runs]
        total_distance = sum(distances)
        avg_distance = mean(distances)
        return (
            f"Total Runs: {len(runs)}\n"
            f"Total Distance: {total_distance:.2f} km\n"
            f"Average Distance: {avg_distance:.2f} km"
        )
