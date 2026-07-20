import sqlite3

conn = sqlite3.connect("database/ecommerce.db")


def test_invalid_order_id():
    result = conn.execute("""
        SELECT COUNT(*)
        FROM order_items oi
        LEFT JOIN orders o
        ON oi.order_id = o.order_id
        WHERE o.order_id IS NULL;
    """).fetchone()[0]

    print("Test 1 - Invalid order_id:", result)


def test_discount_greater_than_100():
    result = conn.execute("""
        SELECT COUNT(*)
        FROM order_items
        WHERE discount_percent > 100;
    """).fetchone()[0]

    print("Test 2 - Discount > 100:", result)


def test_zero_quantity():
    result = conn.execute("""
        SELECT COUNT(*)
        FROM order_items
        WHERE quantity = 0;
    """).fetchone()[0]

    print("Test 3 - Quantity = 0:", result)


def test_future_order_date():
    result = conn.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE DATE(order_date) > DATE('now');
    """).fetchone()[0]

    print("Test 4 - Future order_date:", result)


if __name__ == "__main__":
    test_invalid_order_id()
    test_discount_greater_than_100()
    test_zero_quantity()
    test_future_order_date()

    conn.close()