from ta.momentum import RSIIndicator
from ta.trend import MACD, EMAIndicator
from ta.volatility import BollingerBands


def compute_indicators(df):
    """
    Compute various technical indicators: RSI, MACD, signal, EMA20, Bollinger Bands.
    :param df: DataFrame containing 'close' price column
    :return: DataFrame with additional indicator columns
    """
    # RSI
    rsi_indicator = RSIIndicator(df["close"])
    df["rsi"] = rsi_indicator.rsi()

    # MACD and signal
    macd_indicator = MACD(df["close"])
    df["macd"] = macd_indicator.macd()
    df["signal"] = macd_indicator.macd_signal()

    # EMA 20-day
    ema_indicator = EMAIndicator(df["close"], window=20)
    df["ema20"] = ema_indicator.ema_indicator()

    # Bollinger Bands
    bollinger = BollingerBands(df["close"], window=20)
    df["bb_high"] = bollinger.bollinger_hband()
    df["bb_low"] = bollinger.bollinger_lband()
    df["bb_mid"] = bollinger.bollinger_mavg()

    return df
