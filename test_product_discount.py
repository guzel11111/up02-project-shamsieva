from datetime import date
from models import Product


product = Product(
    product_id=4,
    name="Говядина",
    category="Мясо",
    expiry_date="2026-10-03",
    price=500,
    quantity=8,
    photo=None
)

print("Обычная цена:", product.price)
print(
    "Цена с автоматической скидкой:",
    product.price_with_discount_auto(date(2026, 10, 15))
)