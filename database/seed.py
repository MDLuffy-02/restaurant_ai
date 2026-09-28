from pathlib import Path
from config.database import get_connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    schema_path = Path(__file__).parent / "schema.sql"

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    statements = [
        statement.strip()
        for statement in schema.split(";")
        if statement.strip()
    ]

    try:
        for statement in statements:
            cursor.execute(statement)

        connection.commit()

        print("All database tables created successfully!")

    except Exception as e:
        connection.rollback()
        print(f"Error creating tables: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_tables()