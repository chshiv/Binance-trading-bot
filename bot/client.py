from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        if not self.api_key or not self.api_secret:
            raise Exception("Missing API credentials in .env file")

        self.client = Client(self.api_key, self.api_secret, testnet=True)

    def futures_create_order(self, symbol, side, type, quantity, price=None, timeInForce=None):
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=type,
                quantity=quantity,
                price=price,
                timeInForce=timeInForce
            )

            if not response:
                raise Exception("Empty response from Binance API")

            return response

        except Exception as e:
            raise Exception(f"[BINANCE API ERROR] {str(e)}")