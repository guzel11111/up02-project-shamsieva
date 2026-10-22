
"""Загрузка заказов из PostgreSQL."""

import psycopg
from config import DB_CONFIG
from models import Product, Order


def get_all_orders():
    """Возвращает список объектов Order."""

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    z.id,
                    z.дата,
                    z.клиент,
                    z.количество,
                    t.id,
                    t.наименование,
                    t.категория,
                    t.срок_годности,
                    t.цена,
                    t.количество,
                    t.фото
                FROM "Заказ" AS z
                JOIN "Товар" AS t ON z.товар_id = t.id
                ORDER BY z.id
            """)
            rows = cur.fetchall()

    orders = []

    for row in rows:
        product = Product(
            product_id=row[4],
            name=row[5],
            category=row[6],
            expiry_date=row[7],
            price=row[8],
            quantity=row[9],
            photo=row[10]
        )

        order = Order(
            order_id=row[0],
            date=row[1],
            client=row[2],
            product=product,
            quantity=row[3]
        )

        orders.append(order)

    return orders


def print_orders(orders):
    """Выводит список заказов."""

    print(f"\nВсего заказов: {len(orders)}\n")

    for order in orders:
        print(order.info())
        print("-" * 60)


if __name__ == "__main__":
    orders = get_all_orders()
    print_orders(orders)
