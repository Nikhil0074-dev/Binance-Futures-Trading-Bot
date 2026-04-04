from binance.client import Client
from binance.exceptions import BinanceAPIException
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    base_url = os.getenv("BASE_URL")
    
    if not api_key or not api_secret:
        raise ValueError("API_KEY and API_SECRET must be set in .env")
    
    client = Client(api_key, api_secret, testnet=True)
    if base_url:
        client.API_URL = base_url
    return client
