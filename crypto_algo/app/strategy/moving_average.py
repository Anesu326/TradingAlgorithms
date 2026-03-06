import pandas as pd

def generate_signal(candles):

    df = pd.DataFrame(candles, columns=[
        "time","open","high","low","close","volume"
    ])

    df["fast"] = df["close"].rolling(20).mean()
    df["slow"] = df["close"].rolling(50).mean()

    if df["fast"].iloc[-1] > df["slow"].iloc[-1]:
        return "BUY"

    elif df["fast"].iloc[-1] < df["slow"].iloc[-1]:
        return "SELL"

    return "HOLD"