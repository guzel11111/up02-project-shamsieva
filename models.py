
"""Модели данных для проекта УП.02."""


from datetime import date
from discount import calculate_price_with_discount
class Product:
    """Класс Товар."""

    def __init__(self, product_id, name, category, expiry_date,
                 price, quantity, photo):
        self.id = product_id
        self.name = name
        self.category = category
        self.expiry_date = expiry_date
        self.price = price
        self.quantity = quantity
        self.photo = photo

    def total(self):
        return self.price * self.quantity

    def discounted_price(self):
        """Цена со скидкой 25% (упрощённо)."""
        return self.price * 0.75

    def price_with_discount(self, discount_percent):
        return self.price * (1 - discount_percent / 100)

    def price_with_discount_auto(self, calculation_date=None):
        """Автоматически рассчитывает скидку 25%, если в предыдущем месяце не было заказов."""
        if calculation_date is None:
            calculation_date = date.today()

        return calculate_price_with_discount(
            self.id,
            self.price,
            calculation_date
        )

    def indicator(self):
        return "много" if self.quantity > 5 else "мало"

    def info(self):
        return (
            f"{self.name} ({self.category}): "
            f"{self.price} руб. × {self.quantity} = "
            f"{self.total()} руб. ({self.indicator()})"
        )

    def is_available(self):
        """Проверяет наличие товара."""
        return self.quantity > 0


class Order:
    """Класс Заказ."""

    def __init__(self, order_id, date, client, product, quantity):
        self.id = order_id
        self.date = date
        self.client = client
        self.product = product
        self.quantity = quantity

    def total(self):
        """Стоимость заказа."""
        return self.product.price * self.quantity

    def info(self):
        """Информация о заказе."""
        return (
            f"Заказ №{self.id} от {self.date}: "
            f"{self.client} — {self.product.name} × {self.quantity}; "
            f"сумма: {self.total()} руб."
        )

