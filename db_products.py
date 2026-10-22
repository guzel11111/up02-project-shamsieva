
"""Загрузка товаров из PostgreSQL в объекты Product."""

import psycopg
from config import DB_CONFIG
from models import Product


def get_all_products():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, наименование, категория, срок_годности,
                       цена, количество, фото
                FROM "Товар"
                ORDER BY id
            """)
            rows = cur.fetchall()

    return [
        Product(
            product_id=row[0],
            name=row[1],
            category=row[2],
            expiry_date=row[3],
            price=row[4],
            quantity=row[5],
            photo=row[6]
        )
        for row in rows
    ]


def get_products_by_category(category):
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, наименование, категория, срок_годности,
                       цена, количество, фото
                FROM "Товар"
                WHERE категория = %s
                ORDER BY id
            """, (category,))
            rows = cur.fetchall()

    return [
        Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        for row in rows
    ]


def get_products_low_stock():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, наименование, категория, срок_годности,
                       цена, количество, фото
                FROM "Товар"
                WHERE количество <= 3
                ORDER BY id
            """)
            rows = cur.fetchall()

    return [
        Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        for row in rows
    ]


def print_catalog_with_highlight(products):
    print(f"\n{'=' * 70}")
    print(f"КАТАЛОГ ({len(products)} товаров)")
    print("=" * 70)

    for p in products:
        highlight = "⚠️" if p.quantity <= 3 else "  "
        print(f"{highlight} {p.info()}")
        print(f"   Срок годности: {p.expiry_date}")
        print("-" * 70)

    print("=" * 70)


if __name__ == "__main__":
    print("1. Все товары:")
    print_catalog_with_highlight(get_all_products())

    print("\n2. Товары категории «Молочное»:")
    print_catalog_with_highlight(get_products_by_category("Молочное"))

    print("\n3. Товары с низким остатком (≤ 3):")
    print_catalog_with_highlight(get_products_low_stock())
