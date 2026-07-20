import sqlite3
from datetime import datetime, timedelta


def get_previous_period(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    days = (end - start).days + 1

    previous_end = start - timedelta(days=1)
    previous_start = previous_end - timedelta(days=days - 1)

    return (
        previous_start.strftime("%Y-%m-%d"),
        previous_end.strftime("%Y-%m-%d")
    )


def percentage_change(current, previous):
    if previous == 0:
        return 0
    return round(((current - previous) / previous) * 100, 2)


# Connect to database
conn = sqlite3.connect("database/ecommerce.db")

# User Input
report_type = input("Enter Report Type (daily/weekly/monthly): ")
start_date = input("Enter Start Date (YYYY-MM-DD): ")
end_date = input("Enter End Date (YYYY-MM-DD): ")

previous_start, previous_end = get_previous_period(start_date, end_date)

# Current Period Summary
orders, revenue, customers = conn.execute("""
SELECT
    COUNT(DISTINCT o.order_id),
    ROUND(SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ), 2),
    COUNT(DISTINCT o.customer_id)
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
WHERE DATE(o.order_date) BETWEEN ? AND ?;
""", (start_date, end_date)).fetchone()

orders = orders or 0
revenue = revenue or 0
customers = customers or 0

# Previous Period Summary
prev_orders, prev_revenue, prev_customers = conn.execute("""
SELECT
    COUNT(DISTINCT o.order_id),
    ROUND(SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ), 2),
    COUNT(DISTINCT o.customer_id)
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
WHERE DATE(o.order_date) BETWEEN ? AND ?;
""", (previous_start, previous_end)).fetchone()

prev_orders = prev_orders or 0
prev_revenue = prev_revenue or 0
prev_customers = prev_customers or 0

# Top 3 Products
top_products = conn.execute("""
SELECT
    p.product_name,
    ROUND(SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ), 2) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN orders o
ON o.order_id = oi.order_id
WHERE o.order_date BETWEEN ? AND ?
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 3;
""", (start_date, end_date)).fetchall()

# Report
print("\n========== SALES REPORT ==========")
print(f"Report Type : {report_type}")
print(f"Date Range  : {start_date} to {end_date}")

print("\nSummary")
print(f"Total Orders      : {orders}")
print(f"Total Revenue     : {revenue}")
print(f"Unique Customers  : {customers}")

print("\nTop 3 Products")
for i, (product, product_revenue) in enumerate(top_products, start=1):
    print(f"{i}. {product} - {product_revenue}")

print("\nComparison with Previous Period")
print(f"Orders Change     : {percentage_change(orders, prev_orders)}%")
print(f"Revenue Change    : {percentage_change(revenue, prev_revenue)}%")
print(f"Customer Change   : {percentage_change(customers, prev_customers)}%")

conn.close()