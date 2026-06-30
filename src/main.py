from config import Config
from market import Market
from state_manager import StateManager

config = Config()
market = Market(config.symbol)
state = StateManager()

current = market.get_latest_close(config.lookback_days)
highest = market.get_highest_close(config.lookback_days)

print("=" * 50)
print("Current Close :", current)
print("Highest Close :", highest)
print("Stored High   :", state.get_highest_close())
print("=" * 50)

if highest > state.get_highest_close():
    print("New highest detected.")

    state.set_highest_close(highest)
    state.reset_alerts()
    state.save()

    print("State updated.")