import argparse
import sys
from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(
        description="Trading Bot CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    # This ensures unknown arguments throw error
    args, unknown = parser.parse_known_args()

    if unknown:
        print(f"\n Unknown/extra arguments: {' '.join(unknown)}")
        print("Use --help to see valid options.\n")
        sys.exit(1)
    
    logger.info(f"[CLI INPUT] symbol={args.symbol} side={args.side} "
        f"type={args.type} quantity={args.quantity} price={args.price}")

    try:
        # Validate input
        symbol, side, order_type = validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        client = BinanceClient()

        # Place order
        if order_type == "MARKET":
            response = place_market_order(client, symbol, side, args.quantity)
        else:
            response = place_limit_order(client, symbol, side, args.quantity, args.price)
        
        print(response)

        # Clean output
        print("\n========== ORDER RESULT ==========")
        print(f"Symbol       : {symbol}")
        print(f"Side         : {side}")
        print(f"Type         : {order_type}")
        print(f"Quantity     : {args.quantity}")

        print("\n---------- RESPONSE ----------")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")
        print("=================================\n")

    except Exception as e:
        logger.error(f"[ERROR] {str(e)}")
        print("\n Failed to place order")
        print(f"Reason: {str(e)}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()