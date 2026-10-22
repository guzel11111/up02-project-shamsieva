
import sqlite3
import psycopg
from psycopg import sql
from config import DB_CONFIG
from pathlib import Path

SQLITE_FILE = Path(__file__).parent / "db_variant_29.db"


def migrate():
    with sqlite3.connect(SQLITE_FILE) as source:
        source.row_factory = sqlite3.Row

        with psycopg.connect(**DB_CONFIG) as target:
            with target.cursor() as cur:
                for table in ["Товар", "Пользователь", "Заказ"]:
                    rows = source.execute(
                        f'SELECT * FROM "{table}"'
                    ).fetchall()

                    source_columns = [
                        column["name"]
                        for column in source.execute(
                            f'PRAGMA table_info("{table}")'
                        ).fetchall()
                    ]

                    cur.execute(
                        """
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_schema = 'public'
                          AND table_name = %s
                        """,
                        (table,)
                    )
                    target_columns = {
                        row[0] for row in cur.fetchall()
                    }

                    missing = [
                        col for col in source_columns
                        if col not in target_columns
                    ]

                    if missing:
                        print(
                            f"Таблица «{table}»: "
                            f"не хватает столбцов: {', '.join(missing)}"
                        )
                        continue

                    if not rows:
                        print(f"{table}: записей нет")
                        continue

                    query = sql.SQL(
                        "INSERT INTO {} ({}) VALUES ({}) "
                        "ON CONFLICT DO NOTHING"
                    ).format(
                        sql.Identifier(table),
                        sql.SQL(", ").join(
                            sql.Identifier(col)
                            for col in source_columns
                        ),
                        sql.SQL(", ").join(
                            sql.Placeholder()
                            for _ in source_columns
                        )
                    )

                    for row in rows:
                        cur.execute(
                            query,
                            tuple(row[col] for col in source_columns)
                        )

                    print(
                        f"{table}: обработано записей — {len(rows)}"
                    )

    print("Проверка завершена.")


if __name__ == "__main__":
    try:
        migrate()
    except Exception as error:
        print("Ошибка:", error)
