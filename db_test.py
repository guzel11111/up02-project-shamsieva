
"""Проверка подключения к PostgreSQL."""

import psycopg
from config import DB_CONFIG


def test_connection():
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                print("✅ Подключение к PostgreSQL установлено")

                cur.execute('SELECT COUNT(*) FROM "Товар"')
                count = cur.fetchone()[0]
                print(f"📦 Товаров в базе: {count}")

        print("✅ Соединение закрыто")

    except Exception as e:
        print(f"❌ Ошибка БД: {e}")


if __name__ == "__main__":
    test_connection()
