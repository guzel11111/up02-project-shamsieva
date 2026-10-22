
"""Проверка класса Product."""

from models import Product

p = Product(
    product_id=1,
    name="Кефир",
    category="Молочное",
    expiry_date="2026-10-10",
    price=90,
    quantity=40,
    photo=None
)

print(p.info())
print(f"Со скидкой 25%: {p.price_with_discount(25):.2f} руб.")
print(f"Товар в наличии: {p.is_available()}")