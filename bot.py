import MetaTrader5 as mt5
import talib

# Connect to MetaTrader 5 terminal
mt5.initialize()


def check_signal(symbol):
    # Define parameters
    timeframe = mt5.TIMEFRAME_M5
    ma_fast_period = 50
    ma_slow_period = 200
    ema_fast_period = 13
    ema_slow_period = 35

    # Get the price data for the specified symbol and timeframe
    price_data = mt5.copy_rates_from_pos(symbol, timeframe, 0, 201)

    # Calculate the moving averages
    ma_fast = talib.SMA(price_data["close"], ma_fast_period)
    ma_slow = talib.SMA(price_data["close"], ma_slow_period)
    ema_fast = talib.EMA(price_data["close"], ema_fast_period)
    ema_slow = talib.EMA(price_data["close"], ema_slow_period)

    # Check for long signal
    if ma_fast[-1] > ma_slow[-1] and ema_fast[-1] > ema_slow[-1]:
        print(f"Long signal detected for {symbol}")

    # Check for short signal
    elif ma_slow[-1] > ma_fast[-1] and ema_slow[-1] > ema_fast[-1]:
        print(f"Short signal detected for {symbol}")

    # No signal detected
    # else:
    #     print(f"No signal detected for {symbol}")


# List of symbols to check
symbols = ["EURUSD", "GBPUSD", "AUDUSD", "NZDUSD", "USDCHF", "USDJPY", "USDCAD"]

# Check signals for each symbol
for symbol in symbols:
    check_signal(symbol)

# Disconnect from MetaTrader 5 terminal
mt5.shutdown()
