import requests
import pandas as pd
import time


def fetch_history(symbol, exch, days=30, retries=3):
    """
    Fetch past N days of closing prices from Binance or OKX.
    Implements simple retry logic to handle transient network issues.
    """
    if exch == "Binance":
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&limit={days}"
    elif exch == "OKX":
        url = f"https://www.okx.com/api/v5/market/candles?instId={symbol}&bar=1D"
    else:
        raise ValueError("Unknown exchange")

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            if exch == "Binance":
                data = response.json()
                df = pd.DataFrame(data, columns=[
                    "open_time","open","high","low","close","volume",
                    "close_time","qav","num_trades","taker_base","taker_quote","ignore"
                ])
                df["close"] = df["close"].astype(float)
                return df[["close"]]
            else:  # OKX
                data = response.json().get("data", [])
                df = pd.DataFrame(data, columns=[
                    "ts","open","high","low","close","volume","volCcy","volCcyQuote","confirm"
                ])
                df["close"] = df["close"].astype(float)
                return df[["close"]]
        except Exception:
            # if not last attempt, wait and retry
            if attempt < retries - 1:
                time.sleep(2)
                continue
            else:
                # propagate exception on final failure
                raise
