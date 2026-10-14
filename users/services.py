import stripe
from forex_python.converter import CurrencyRates

from config.settings import STRIPE_API_KEY

stripe_api_key = STRIPE_API_KEY

c = CurrencyRates()

def create_stripe_product(name):
    """Создаём продукт в Stripe"""
    return stripe.Product.create(name=name)

# def convert_rub_to_dollars(amount_rub):
#
#     rate = c.get_rate('RUB', 'USD')
#     return amount_rub * rate

def create_stripe_price(product_id, amount_rub):
    """
    Создаём цену в Stripe.
    """
    unit_amount = int(round(amount_rub * 100))
    return stripe.Price.create(
        currency="rub",
        unit_amount=unit_amount,
        product=product_id,
    )

def create_stripe_session(price_id, success_url, cancel_url):
    session = stripe.checkout.Session.create(
        success_url=success_url,
        cancel_url=cancel_url,
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url
