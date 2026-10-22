
"""Тестирование алгоритма расчёта скидки."""

from datetime import date
from discount import (
    get_previous_month_range,
    has_orders_in_previous_month,
    calculate_price_with_discount
)


def run_tests():
    calculation_date = date(2026, 10, 15)

    start, end = get_previous_month_range(calculation_date)
    print(f"Проверяем период: {start} — {end}")

    # Тестируем товары, которые действительно есть в нашей БД.
    with_orders = []
    without_orders = []

    for product_id in range(1, 8):
        if has_orders_in_previous_month(product_id, calculation_date):
            with_orders.append(product_id)
        else:
            without_orders.append(product_id)

    print("Товары с заказами в сентябре:", with_orders)
    print("Товары без заказов в сентябре:", without_orders)

    print("\nПримеры расчёта:")
    print(
        "Цена 8500 при наличии заказов:",
        calculate_price_with_discount(1, 8500, calculation_date)
    )
    print(
        "Цена 15000 без заказов:",
        calculate_price_with_discount(999, 15000, calculation_date)
    )


if __name__ == "__main__":
    run_tests()
