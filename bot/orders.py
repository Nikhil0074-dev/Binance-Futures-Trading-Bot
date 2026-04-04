import logging
from .client import get_client
from .validators import validate_side, validate_order_type, validate_quantity, validate_price

logger = logging.getLogger(__name__)

def place_order(symbol, side, order_type, quantity, price=None):
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    validate_price(price, order_type)
    
    try:
        client = get_client()
        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        order = client.futures_create_order(**params)
        logger.info(f"Order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
