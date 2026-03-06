import ccxt
from config import API_KEY, SECRET

exchange = ccxt.binance({
    "apiKey": API_KEY,
    "secret": SECRET,
    "enableRateLimit": True
})