import json
from pathlib import Path


class Config:
    def __init__(self):
        config_file = Path("config.json")

        if not config_file.exists():
            raise FileNotFoundError("config.json not found")

        with open(config_file, "r") as file:
            self.data = json.load(file)

    @property
    def symbol(self):
        return self.data["market"]["symbol"]

    @property
    def lookback_days(self):
        return self.data["market"]["lookback_days"]

    @property
    def levels(self):
        return self.data["alerts"]["levels"]

    @property
    def notification_provider(self):
        return self.data["notification"]["provider"]