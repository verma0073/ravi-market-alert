import yfinance as yf


def get_market_data(symbol: str):
    """
    Fetch latest market data and historical high.
    """

    ticker = yf.Ticker(symbol)

    # Get last 1 year data
    hist = ticker.history(period="1y")

    if hist.empty:
        raise Exception(f"No market data found for symbol: {symbol}")

    current_close = float(hist["Close"].iloc[-1])
    historical_high = float(hist["Close"].max())

    return {
        "current_close": current_close,
        "historical_high": historical_high
    }