"""
Simple Moving Average Crossover Backtest
----------------------------------------
Market: BTC-USD (via Yahoo Finance)
Timeframe: Daily
Strategy: Long-only MA crossover
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# =========================
# PARAMETERS
# =========================
SYMBOL = "BTC-USD"
START_DATE = "2020-01-01"
SHORT_WINDOW = 20
LONG_WINDOW = 50
ANNUALIZATION_FACTOR = 252  # trading days

# =========================
# DATA LOADING
# =========================
data = yf.download(SYMBOL, start=START_DATE)

data = data[['Close']]
data.dropna(inplace=True)

# =========================
# INDICATORS
# =========================
data['ma_short'] = data['Close'].rolling(SHORT_WINDOW).mean()
data['ma_long'] = data['Close'].rolling(LONG_WINDOW).mean()

# =========================
# SIGNAL GENERATION
# =========================
data['signal'] = 0
data.loc[data['ma_short'] > data['ma_long'], 'signal'] = 1

# Shift signal to avoid look-ahead bias
data['signal'] = data['signal'].shift(1)
data.dropna(inplace=True)

# =========================
# RETURNS
# =========================
data['market_return'] = data['Close'].pct_change()
data['strategy_return'] = data['signal'] * data['market_return']

# =========================
# EQUITY CURVES
# =========================
data['equity_market'] = (1 + data['market_return']).cumprod()
data['equity_strategy'] = (1 + data['strategy_return']).cumprod()

# =========================
# PERFORMANCE METRICS
# =========================
total_return = data['equity_strategy'].iloc[-1] - 1

rolling_max = data['equity_strategy'].cummax()
drawdown = data['equity_strategy'] / rolling_max - 1
max_drawdown = drawdown.min()

sharpe_ratio = (
    data['strategy_return'].mean() /
    data['strategy_return'].std()
) * np.sqrt(ANNUALIZATION_FACTOR)

# =========================
# OUTPUT
# =========================
print("===== STRATEGY PERFORMANCE =====")
print(f"Symbol: {SYMBOL}")
print(f"Total Return: {total_return:.2%}")
print(f"Max Drawdown: {max_drawdown:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# =========================
# PLOTS
# =========================
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['equity_market'], label='Buy & Hold')
plt.plot(data.index, data['equity_strategy'], label='MA Strategy')
plt.legend()
plt.title("Equity Curve")
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Price')
plt.plot(data.index, data['ma_short'], label='Short MA')
plt.plot(data.index, data['ma_long'], label='Long MA')
plt.legend()
plt.title("Price & Moving Averages")
plt.show()
