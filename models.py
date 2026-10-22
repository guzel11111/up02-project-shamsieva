
"""Модели данных для проекта УП.02."""


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
        """Общая стоимость товара на складе."""
        return self.price * self.quantity

    def price_with_discount(self, discount_percent):
        """Цена товара со скидкой."""
        return self.price * (1 - discount_percent / 100)

    def indicator(self):
        """Остаток товара: много или мало."""
        return "много" if self.quantity > 5 else "мало"

    def info(self):
        """Информация о товаре."""
        return (
            f"{self.name} ({self.category}): "
            f"{self.price} руб. × {self.quantity} = "
            f"{self.total()} руб. ({self.indicator()})"
        )
