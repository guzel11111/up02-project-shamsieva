
"""Расчёт скидки на товары по истории заказов."""

from datetime import timedelta
import psycopg
from config import DB_CONFIG


def get_previous_month_range(date):
    """Возвращает начало и конец предыдущего календарного месяца."""
    first_day = date.replace(day=1)
    last_day_prev = first_day - timedelta(days=1)
    first_day_prev = last_day_prev.replace(day=1)

    return first_day_prev, last_day_prev


def has_orders_in_previous_month(product_id, date):
    """Проверяет, были ли заказы товара в предыдущем месяце."""
    start, end = get_previous_month_range(date)

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT COUNT(*)
                FROM "Заказ"
                WHERE товар_id = %s
                  AND дата BETWEEN %s AND %s
                """,
                (product_id, start, end)
            )
            count = cur.fetchone()[0]

    return count > 0


def calculate_price_with_discount(product_id, price, date):
    """Скидка 25%, если в предыдущем месяце заказов не было."""
    if has_orders_in_previous_month(product_id, date):
        return price

    return round(price * 0.75, 2)
