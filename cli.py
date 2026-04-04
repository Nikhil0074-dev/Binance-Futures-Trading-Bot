import click
import logging
from bot.logging_config import setup_logger
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price

# Setup logging
setup_logger()

logger = logging.getLogger(__name__)

@click.command()
@click.option("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
@click.option("--side", required=True, type=click.Choice(["BUY", "SELL"]), help="Order side")
@click.option("--order_type", required=True, type=click.Choice(["MARKET", "LIMIT"]), help="Order type")
@click.option("--quantity", type=float, required=True, help="Order quantity")
@click.option("--price", type=float, default=None, help="Price for LIMIT orders")

def main(symbol, side, order_type, quantity, price):
    """
    Binance Futures Trading Bot CLI
    """
    try:
        click.echo("\n Order Summary")
        click.echo(f"Symbol: {symbol}")
        click.echo(f"Side: {side}")
        click.echo(f"Type: {order_type}")
        click.echo(f"Quantity: {quantity}")
        if price:
            click.echo(f"Price: {price}")
        click.echo()

        # Place order
        order = place_order(symbol, side, order_type, quantity, price)

        click.echo(" Order Placed Successfully!")
        click.echo(f"Order ID: {order.get('orderId', 'N/A')}")
        click.echo(f"Status: {order.get('status', 'N/A')}")
        click.echo(f"Executed Qty: {order.get('executedQty', 'N/A')}")
        click.echo(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        click.echo(f" Error: {str(e)}", err=True)
        logger.error(f"CLI error: {str(e)}")

if __name__ == "__main__":
    main()

