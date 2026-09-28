import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    required = ("DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME")
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError(f"Missing database environment variables: {', '.join(missing)}")

    config = {
        "host": os.environ["DB_HOST"],
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
        "database": os.environ["DB_NAME"],
    }

    ssl_ca = os.getenv("DB_SSL_CA")
    if ssl_ca:
        config.update(ssl_ca=ssl_ca, ssl_verify_cert=True)

    return mysql.connector.connect(**config)
