from .exchange import exchange

def get_candles(symbol="BTC/USDT", timeframe="1m", limit=100):

    candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    return candles