from config import Config

config = Config()

print("=" * 40)
print("Market Symbol :", config.symbol)
print("Lookback Days :", config.lookback_days)
print("Alert Levels  :", config.levels)
print("Notifier      :", config.notification_provider)
print("=" * 40)