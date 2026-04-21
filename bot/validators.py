VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]

# You can expand this list if needed
VALID_SYMBOLS = [
    # Major
    "BTCUSDT", "ETHUSDT", "BNBUSDT",
    "XRPUSDT", "ADAUSDT", "SOLUSDT",

    # Large Cap
    "DOGEUSDT", "DOTUSDT", "MATICUSDT",
    "LTCUSDT", "AVAXUSDT", "LINKUSDT",
    "UNIUSDT", "ATOMUSDT", "XLMUSDT",
    "ETCUSDT", "BCHUSDT", "ALGOUSDT",

    # Mid Cap
    "FILUSDT", "VETUSDT", "ICPUSDT",
    "SANDUSDT", "MANAUSDT", "AXSUSDT",
    "GALAUSDT", "AAVEUSDT", "MKRUSDT",
    "EGLDUSDT", "XTZUSDT", "HBARUSDT",

    # DeFi
    "SUSHIUSDT", "CRVUSDT", "COMPUSDT",
    "SNXUSDT", "YFIUSDT", "1INCHUSDT",
    "BALUSDT", "RUNEUSDT", "LRCUSDT",

    # Layer 2 / Infra
    "OPUSDT", "ARBUSDT", "APTUSDT",
    "SUIUSDT", "STXUSDT", "INJUSDT",
    "NEARUSDT", "FTMUSDT", "FLOWUSDT",

    # Meme
    "SHIBUSDT", "PEPEUSDT", "FLOKIUSDT",
]

def normalize_inputs(symbol, side, order_type):
    """
    Convert inputs to uppercase for consistency
    """
    return symbol.upper(), side.upper(), order_type.upper()


def validate_order(symbol, side, order_type, quantity, price):
    # Normalize
    symbol, side, order_type = normalize_inputs(symbol, side, order_type)

    # Symbol validation
    if symbol not in VALID_SYMBOLS:
        raise ValueError(f"Invalid symbol '{symbol}'. Available symbols: {', '.join(VALID_SYMBOLS)}")

    # Side validation
    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side '{side}'. Allowed values: BUY / SELL")

    # Order type validation
    if order_type not in VALID_TYPES:
        raise ValueError(f"Invalid order type '{order_type}'. Allowed: MARKET / LIMIT")

    # Quantity validation
    if quantity is None:
        raise ValueError("Quantity is required")

    if not isinstance(quantity, (int, float)):
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # Price validation
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return symbol, side, order_type