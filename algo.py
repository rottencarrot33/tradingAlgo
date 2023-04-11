import MetaTrader5 as mt5
import pandas as pd

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

    # Convert price_data to a pandas DataFrame
    df = pd.DataFrame(price_data)

    # Add the moving averages to the DataFrame
    df['MA Fast'] = df['close'].rolling(ma_fast_period).mean()
    df['MA Slow'] = df['close'].rolling(ma_slow_period).mean()
    df['EMA Fast'] = df['close'].ewm(span=ema_fast_period).mean()
    df['EMA Slow'] = df['close'].ewm(span=ema_slow_period).mean()

    # Check for long signal
    if df['MA Fast'].iloc[-1] > df['MA Slow'].iloc[-1] and df['EMA Fast'].iloc[-1] > df['EMA Slow'].iloc[-1]:
        print(f"Long signal detected for {symbol}")

    # Check for short signal
    elif df['MA Slow'].iloc[-1] > df['MA Fast'].iloc[-1] and df['EMA Slow'].iloc[-1] > df['EMA Fast'].iloc[-1]:
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
