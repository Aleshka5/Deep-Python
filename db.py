import psycopg2
import traceback
from psycopg2.extras import DictCursor
import time

DATABASE_URL = (
    "dbname=nordwind user=student password=qweasd963 host=95.163.241.236 port=5432"
)


def db_connection(func):
    """
    Decorator for database connection management.
    """

    def wrapper(*args, **kwargs):
        while True:
            try:
                conn = psycopg2.connect(DATABASE_URL)
                break
            except Exception as e:
                print(f"Connection failed, retrying: {e}")
                time.sleep(1)

        try:
            with conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    response = func(*args, **kwargs, cursor=cursor)

        except Exception as er:
            response = {
                "status": "Error",
                "message": str(er),
                "traceback": traceback.format_exc(),
            }

        finally:
            conn.close()
            return response

    return wrapper


@db_connection
def request(cursor=None):
    query = """
        SELECT product_name
        FROM products
        WHERE unit_price >= %s AND unit_price < %s
    """
    min_price = 3
    max_price = 7
    cursor.execute(query, (min_price, max_price))
    rows = cursor.fetchall()
    return rows  # [dict(row)["name"] for row in rows]


@db_connection
def get_min_price_by_category(category_id, cursor=None):
    query = """
        SELECT MIN(unit_price) AS min_price
        FROM products
        WHERE category_id = %s;
    """
    cursor.execute(query, (category_id,))
    row = cursor.fetchone()
    return row["min_price"]


@db_connection
def get_max_price_by_suppliers(cursor=None):
    query = """
        SELECT supplier_id, MAX(unit_price) AS max_price
        FROM products
        WHERE supplier_id IN (1, 3, 5)
        GROUP BY supplier_id
        ORDER BY supplier_id;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    return [
        {"supplier_id": row["supplier_id"], "max_price": row["max_price"]}
        for row in rows
    ]
