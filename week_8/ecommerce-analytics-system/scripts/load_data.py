import sqlite3
import pandas as pd


# Connect to SQLite Database
connection = sqlite3.connect("database/ecommerce.db")


# Create Tables from Schema
with open("sql/schema.sql", "r") as file:
    schema = file.read()

connection.executescript(schema)


# Read Cleaned CSV Files
customers_df = pd.read_csv("data/cleaned/customers.csv")
products_df = pd.read_csv("data/cleaned/products.csv")
orders_df = pd.read_csv("data/cleaned/orders.csv")
order_items_df = pd.read_csv("data/cleaned/order_items.csv")


# Load Data into SQLite Tables
customers_df.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False
)

products_df.to_sql(
    "products",
    connection,
    if_exists="replace",
    index=False
)

orders_df.to_sql(
    "orders",
    connection,
    if_exists="replace",
    index=False
)

order_items_df.to_sql(
    "order_items",
    connection,
    if_exists="replace",
    index=False
)


# Save Changes
connection.commit()


# Verify Data Loaded
print("\nData Loaded Successfully")
print("-" * 30)

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

for table in tables:
    count = connection.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table}: {count} rows")


# Close Connection
connection.close()