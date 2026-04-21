# 🤖 Binance Futures Trading Bot

A simplified trading bot built for **Binance Futures Testnet (USDT-M)**. Supports Market and Limit orders via a clean CLI interface, with structured logging and robust error handling.

---

## 📁 Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order placement logic (market & limit)
│   ├── validators.py      # Input validation and normalization
│   └── logging_config.py  # Logging setup
├── cli.py                 # CLI entry point (argparse)
├── .env                   # API credentials (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/trading_bot.git
cd trading_bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Binance Futures Testnet Credentials

1. Register at [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Generate your API Key and Secret
3. Create a `.env` file in the project root:

```env
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_api_secret_here
```

> ⚠️ **Never commit your `.env` file.** It is already included in `.gitignore`.

---

## 🚀 How to Run

### Place a Market Order

```bash
# BUY 0.01 BTC at market price
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# SELL 0.05 ETH at market price
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.05
```

### Place a Limit Order

```bash
# BUY 0.01 BTC with a limit price of 30000
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000

# SELL 0.1 SOL with a limit price of 20
python cli.py --symbol SOLUSDT --side SELL --type LIMIT --quantity 0.1 --price 20
```

### CLI Arguments

| Argument     | Required | Description                              |
|--------------|----------|------------------------------------------|
| `--symbol`   | ✅        | Trading pair (e.g. `BTCUSDT`)            |
| `--side`     | ✅        | `BUY` or `SELL`                          |
| `--type`     | ✅        | `MARKET` or `LIMIT`                      |
| `--quantity` | ✅        | Order quantity (must be > 0)             |
| `--price`    | ⚠️ LIMIT only | Limit price (required for LIMIT orders) |

---

## 📊 Sample Output

```
============================================================
           BINANCE FUTURES TESTNET - ORDER SUMMARY
============================================================
  Symbol    : BTCUSDT
  Side      : BUY
  Type      : MARKET
  Quantity  : 0.01
------------------------------------------------------------

✅ Order placed successfully!

  Order ID     : 3951823401
  Status       : FILLED
  Executed Qty : 0.01
  Avg Price    : 43215.20
============================================================
```

---

## 📝 Logging

All API requests, responses, and errors are logged to `trading_bot.log` in the project root.

Log format:
```
2026-04-21 15:32:10,412 - INFO  - [ORDER REQUEST] MARKET | BTCUSDT | BUY | qty=0.01
2026-04-21 15:32:11,083 - INFO  - [ORDER SUCCESS] MARKET | orderId=3951823401 status=FILLED executedQty=0.01
```

Log levels used:
- `INFO` — order requests, successful responses
- `ERROR` — validation failures, API errors, network issues

---

## ✅ Supported Symbols

The bot validates symbols against a predefined list including:

| Category     | Examples                                      |
|--------------|-----------------------------------------------|
| Major        | BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT            |
| Large Cap    | DOGEUSDT, AVAXUSDT, LINKUSDT, DOTUSDT         |
| Mid Cap      | SANDUSDT, AXSUSDT, AAVEUSDT, HBARUSDT         |
| DeFi         | UNIUSDT, CRVUSDT, SUSHIUSDT, COMPUSDT         |
| Layer 2      | OPUSDT, ARBUSDT, NEARUSDT, INJUSDT            |
| Meme         | SHIBUSDT, PEPEUSDT, FLOKIUSDT                 |

---

## 🛠️ Requirements

```
python-binance
python-dotenv
```

Install via:
```bash
pip install -r requirements.txt
```

---

## 📌 Assumptions

- All orders are placed on **Binance Futures Testnet (USDT-M)** using `testnet=True`.
- Limit orders use **GTC (Good Till Cancelled)** as the default `timeInForce`.
- Symbol, side, and order type inputs are **case-insensitive** (normalized to uppercase internally).
- The bot does **not** manage open positions or cancel existing orders — it is order-placement only.
- Quantity and price precision must comply with Binance's symbol rules; invalid precision will return an API error.

---

## 🔒 Security Note

This project is intended for **testnet use only**. Do not use real API credentials or connect to Binance's live trading environment with this bot without additional safeguards.

## 🗂️ Log File
 
The log file below contains real output from the testnet, including at least one **MARKET order** and one **LIMIT order**:
 
📄 [View trading_bot.log on Google Drive](https://drive.google.com/file/d/1qbKgop__xUdOHVAwT2mKs-0Kv4S9hDh1/view?usp=sharing)