from datetime import datetime

class FilterEngine:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def filter_by_date_range(self, start, end):
        runs = self.data_handler.get_runs()
        start_dt = datetime.fromisoformat(start)
        end_dt = datetime.fromisoformat(end)
        return [r for r in runs if start_dt <= datetime.fromisoformat(r["date"]) <= end_dt]
