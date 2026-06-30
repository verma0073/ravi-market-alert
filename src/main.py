from config import load_config
from market import get_market_data
from alert_engine import check_alerts
from notifier import send_notification
from state_manager import load_state, save_state


def main():
    # Load config
    config = load_config()

    symbol = config["market"]["symbol"]
    levels = config["alerts"]["levels"]

    print("============================================================")
    print(f"Market            : {symbol}")

    # Load previous state
    state = load_state()

    # Fetch market data
    data = get_market_data(symbol)

    current_close = data["current_close"]
    highest_close = max(data["historical_high"], state.get("highest_close", 0))

    # Update state
    state["highest_close"] = highest_close
    state["last_close"] = current_close

    # Calculate correction
    correction = ((highest_close - current_close) / highest_close) * 100

    print(f"Current Close     : {current_close:,.2f}")
    print(f"Highest Close     : {highest_close:,.2f}")
    print(f"Correction        : {correction:.2f}%")
    print("============================================================")

    # Check alerts
    triggered = state.get("triggered_levels", [])

    alerts = check_alerts(correction, levels, triggered)

    if alerts:
        print("\nAlerts Triggered")
        for alert in alerts:
            print(f"✅ {alert}% correction reached")
            send_notification(f"Nifty Correction Alert: {alert}% reached")

        # update triggered levels
        triggered.extend(alerts)
        state["triggered_levels"] = list(set(triggered))

    else:
        print("\nNo new alerts triggered")

    # Save updated state
    save_state(state)


if __name__ == "__main__":
    main()