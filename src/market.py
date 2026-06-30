import yfinance as yf


class Market:

    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_history(self, days: int):
        ticker = yf.Ticker(self.symbol)
        return ticker.history(period=f"{days}d")

    def get_latest_close(self, days: int = 365):

        history = self.get_history(days)

        if history.empty:
            raise Exception("No market data received.")

        return float(history["Close"].iloc[-1])

    def get_highest_close(self, days: int = 365):

        history = self.get_history(days)

        if history.empty:
            raise Exception("No market data received.")

        return float(history["Close"].max())