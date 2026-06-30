import json
import os
from typing import Dict, Any

STATE_FILE = "data/state.json"


def load_state() -> Dict[str, Any]:
    """
    Load persisted state from disk.
    Returns empty dict if no state exists.
    """
    if not os.path.exists(STATE_FILE):
        return {}

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If file is corrupted, reset state safely
        return {}


def save_state(state: Dict[str, Any]) -> None:
    """
    Save state atomically to avoid corruption.
    """
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)

    temp_file = STATE_FILE + ".tmp"

    with open(temp_file, "w") as f:
        json.dump(state, f, indent=2)

    os.replace(temp_file, STATE_FILE)