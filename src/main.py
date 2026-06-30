from config import Config
from market import Market

config = Config()

market = Market(config.symbol)

current = market.get_latest_close(config.lookback_days)
highest = market.get_highest_close(config.lookback_days)

print("=" * 40)
print("Market :", config.symbol)
print(f"Current Close : {current:.2f}")
print(f"Highest Close : {highest:.2f}")
print("=" * 40)