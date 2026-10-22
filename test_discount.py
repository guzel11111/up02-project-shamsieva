
"""Расширенное тестирование алгоритма скидки."""

from datetime import date
from discount import (
    get_previous_month_range,
    has_orders_in_previous_month,
    calculate_price_with_discount,
)


def run_tests():
    test_cases = [
        # product_id, price, date, expected, comment
        (1, 8500, date(2026, 10, 15), 8500, "Заказы были в сентябре"),
        (2, 15000, date(2026, 10, 15), 15000, "Заказы были в сентябре"),
        (3, 12000, date(2026, 10, 15), 12000, "Заказы были в сентябре"),
        (4, 4500, date(2026, 10, 15), 3375, "Заказов не было в сентябре"),
        (5, 6000, date(2026, 10, 15), 4500, "Заказов не было в сентябре"),
        (6, 1000, date(2026, 10, 15), 750, "Заказов не было в сентябре"),
        (7, 200, date(2026, 10, 15), 150, "Заказов не было в сентябре"),
        (4, 0, date(2026, 10, 15), 0, "Нулевая цена"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 70)

    start, end = get_previous_month_range(date(2026, 10, 1))
    print(f"Для 01.10.2026 проверяется период: {start} — {end}")

    start, end = get_previous_month_range(date(2026, 10, 31))
    print(f"Для 31.10.2026 проверяется период: {start} — {end}")

    passed = 0

    for product_id, price, calculation_date, expected, comment in test_cases:
        result = calculate_price_with_discount(
            product_id, price, calculation_date
        )

        success = result == expected
        if success:
            passed += 1

        status = "OK" if success else "ОШИБКА"
        print(
            f"{status}: товар {product_id}, дата {calculation_date}, "
            f"цена {price} -> {result}, ожидалось {expected}. {comment}"
        )

    print("-" * 70)
    print(f"Пройдено: {passed} из {len(test_cases)}")

    # Проверяем переход между годами.
    start, end = get_previous_month_range(date(2027, 1, 1))
    print(f"Для 01.01.2027 проверяется период: {start} — {end}")

    if start == date(2026, 12, 1) and end == date(2026, 12, 31):
        print("OK: переход между годами работает")
    else:
        print("ОШИБКА: неверный период при переходе между годами")


if __name__ == "__main__":
    run_tests()

