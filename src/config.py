import json
from typing import Dict, Any

CONFIG_FILE = "config.json"


def load_config() -> Dict[str, Any]:
    """
    Loads configuration from config.json
    """
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)