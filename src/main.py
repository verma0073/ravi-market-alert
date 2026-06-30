from config import Config
from market import Market
from state_manager import StateManager
from alert_engine import AlertEngine

config = Config()
market = Market(config.symbol)
state = StateManager()

current = market.get_latest_close(config.lookback_days)
highest = market.get_highest_close(config.lookback_days)

if highest > state.get_highest_close():
    state.set_highest_close(highest)
    state.reset_alerts()
    state.save()

stored_high = state.get_highest_close()

engine = AlertEngine(state)

correction = engine.calculate_correction(
    current,
    stored_high
)

print("=" * 60)
print(f"Market            : {config.symbol}")
print(f"Current Close     : {current:,.2f}")
print(f"Highest Close     : {stored_high:,.2f}")
print(f"Correction        : {correction:.2f}%")
print("=" * 60)

alerts = engine.check_alerts(
    correction,
    config.levels
)

if alerts:
    print("\nAlerts Triggered")

    for level in alerts:
        print(f"✅ {level}% correction reached")
else:
    print("\nNo alerts.")