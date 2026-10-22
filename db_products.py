
"""Загрузка и вывод каталога товаров из PostgreSQL."""

import psycopg
from config import DB_CONFIG


def get_all_products():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, категория, наименование, срок_годности,
                       цена, количество, фото
                FROM "Товар"
                ORDER BY id
            """)
            return cur.fetchall()


def get_products_by_category(category):
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, категория, наименование, срок_годности,
                       цена, количество, фото
                FROM "Товар"
                WHERE категория = %s
                ORDER BY id
            """, (category,))
            return cur.fetchall()


def get_products_low_stock():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, категория, наименование, срок_годности,
                       цена, количество, фото
                FROM "Товар"
                WHERE количество <= 3
                ORDER BY id
            """)
            return cur.fetchall()


def get_categories():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT DISTINCT категория
                FROM "Товар"
                ORDER BY категория
            """)
            return [row[0] for row in cur.fetchall()]


def print_catalog(products):
    print(f"\n{'=' * 60}")
    print(f"КАТАЛОГ: {len(products)} товаров")
    print("=" * 60)

    for p in products:
        product_id, category, name, expiry_date, price, quantity, photo = p

        indicator = "много" if quantity > 5 else "мало"
        warning = "⚠️" if quantity <= 3 else "  "

        print(f"{warning} {product_id}. {name} ({category})")
        print(f"   Цена: {price} руб. | Остаток: {quantity} шт. ({indicator})")
        print(f"   Срок годности: {expiry_date}")
        print("-" * 60)


if __name__ == "__main__":
    print("1. Все товары")
    print_catalog(get_all_products())

    print("\n2. Категории:")
    for category in get_categories():
        print(f"   - {category}")

    print("\n3. Товары с низким остатком (<= 3):")
    print_catalog(get_products_low_stock())

    print("\n4. Пример фильтрации по категории:")
    categories = get_categories()
    if categories:
        print(f"Категория: {categories[0]}")
        print_catalog(get_products_by_category(categories[0]))
