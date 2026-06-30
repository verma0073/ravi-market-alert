import json
from pathlib import Path


class StateManager:

    def __init__(self):
        self.state_file = Path("data/state.json")

        # Create state.json if it doesn't exist
        if not self.state_file.exists():
            self.state = {
                "highest_close": 0,
                "alerts_sent": {}
            }
            self.save()
        else:
            self.load()

    def load(self):
        with open(self.state_file, "r") as file:
            self.state = json.load(file)

    def save(self):
        with open(self.state_file, "w") as file:
            json.dump(self.state, file, indent=4)

    def get_highest_close(self):
        return self.state["highest_close"]

    def set_highest_close(self, value):
        self.state["highest_close"] = value

    def is_alert_sent(self, level):
        return self.state["alerts_sent"].get(str(level), False)

    def mark_alert_sent(self, level):
        self.state["alerts_sent"][str(level)] = True

    def reset_alerts(self):
        self.state["alerts_sent"] = {}