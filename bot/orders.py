from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(client, symbol, side, quantity):
    try:
        # BUSINESS LOG
        logger.info(f"[ORDER REQUEST] MARKET | {symbol} | {side} | qty={quantity}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        # BUSINESS RESPONSE LOG
        logger.info(
            f"[ORDER SUCCESS] MARKET | orderId={response.get('orderId')} "
            f"status={response.get('status')} executedQty={response.get('executedQty')}"
        )

        return response

    except Exception as e:
        logger.error(f"[ORDER FAILED] MARKET | {symbol} | error={str(e)}")
        raise


def place_limit_order(client, symbol, side, quantity, price):
    try:
        # BUSINESS LOG
        logger.info(f"[ORDER REQUEST] LIMIT | {symbol} | {side} | qty={quantity} | price={price}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        # BUSINESS RESPONSE LOG
        logger.info(
            f"[ORDER SUCCESS] LIMIT | orderId={response.get('orderId')} "
            f"status={response.get('status')} price={price}"
        )

        return response

    except Exception as e:
        logger.error(f"[ORDER FAILED] LIMIT | {symbol} | error={str(e)}")
        raise