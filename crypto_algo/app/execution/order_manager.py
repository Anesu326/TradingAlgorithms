from app.data.exchange import exchange

def place_order(symbol, side, amount):

    if side == "BUY":
        return exchange.create_market_buy_order(symbol, amount)

    if side == "SELL":
        return exchange.create_market_sell_order(symbol, amount)