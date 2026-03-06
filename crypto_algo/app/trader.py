from app.data.market_data import get_candles
from app.strategy.moving_average import generate_signal
from app.execution.order_manager import place_order
from app.state import bot_state

SYMBOL = "BTC/USDT"
AMOUNT = 0.001

def run():

    candles = get_candles(SYMBOL)

    signal = generate_signal(candles)

    if signal == "BUY":
        place_order(SYMBOL, "BUY", AMOUNT)

    elif signal == "SELL":
        place_order(SYMBOL, "SELL", AMOUNT)