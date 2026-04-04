# Binance Futures Trading Bot 

## Setup

1. Clone/Download this repo
2. Copy `.env.example` to `.env` and add your Binance Testnet API keys:
   - Get from https://testnet.binancefuture.com
3. Install dependencies:
   ```
   python -m venv venv
   venv\\Scripts\\activate  # Windows
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```
   python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
   ```

## Examples

**Market Buy:**
```
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

**Limit Sell:**
```
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 60000
```

## Features
- Market & Limit orders (BUY/SELL)
- Input validation & error handling
- Structured logging to `logs/bot.log`
- Binance USDT-M Futures Testnet

## Logs
Check `logs/bot.log` for order history and errors.

## Assumptions
- USDT-M Futures only
- No leverage/position management

