import pandas as pd

customers_df = pd.read_csv("data/raw/customers.csv")
products_df = pd.read_csv("data/raw/products.csv")
orders_df = pd.read_csv("data/raw/orders.csv")
order_items_df = pd.read_csv("data/raw/order_items.csv")

print("===== CUSTOMERS DATA PROFILE =====")

print("\nFirst 5 Rows:")
print(customers_df.head())

print("\nShape:")
print(customers_df.shape)

print("\nColumns:")
print(customers_df.columns)

print("\nData Types:")
print(customers_df.dtypes)

print("\nValue Counts for customer_type:")
print(customers_df["customer_type"].value_counts())

print("\nUnique Values:")
print(customers_df.nunique())

print("\nInfo:")
customers_df.info()

print("\nMissing Values:")
print(customers_df.isnull().sum())

print("\nDuplicate Rows:")
print(customers_df.duplicated().sum())

print("\nSummary Statistics:")
print(customers_df.describe(include="all"))

import re

EMAIL_PATTERN = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

def validate_emails(df):

    invalid_emails = df[
        ~df["email"].str.match(EMAIL_PATTERN)
    ]

    return invalid_emails["customer_id"].tolist()

def clean_customers(df):
    df = df.copy()

    report = {}
    report["Total Rows Processed"] = len(df)

    report["Missing Values"] = df.isnull().sum().sum()

    report["Duplicate Rows"] = df.duplicated().sum()

    df["registration_date"] = pd.to_datetime(
            df["registration_date"]
        )

    print("\nData Types After Cleaning:")
    print(df.dtypes)

    print("\nUnique Customer Types:")
    print(df["customer_type"].unique())

    VALID_CUSTOMER_TYPES = {
        "REGULAR",
        "PREMIUM",
        "VIP"
    }

    invalid_customer_types = df[
        ~df["customer_type"].isin(VALID_CUSTOMER_TYPES)
    ]

    print("\nInvalid Customer Types:")
    print(invalid_customer_types)
    report["Invalid Customer Types"] = len(invalid_customer_types)


    print("\nIds of Customers with Invalid Emails:")
    invalid_customer_ids = validate_emails(df)
    print("Customers with Invalid Emails:")
    print(invalid_customer_ids)
    report["Invalid Emails"] = len(invalid_customer_ids)

    rows_before = len(df)
     
    # Remove rows with invalid emails
    df = df[
        df["email"].str.match(EMAIL_PATTERN)
    ].copy()

    rows_removed = rows_before - len(df)

    report["Rows Removed"] = rows_removed
    report["Rows Remaining"] = len(df)


    # print("\nCustomers Table Cleaning Report:")
    # print("-" * 50)
    # for category, count in report.items():
    #     print(f"{category}: {count}")
    
    # print("\n\n\n")
    
    return df, report

def write_report(table_name, report, mode):

    with open("output/cleaning_report.txt", mode) as file:

        file.write(f"{table_name}\n")
        file.write("-" * len(table_name) + "\n")

        for check, result in report.items():
            file.write(f"{check}: {result}\n")

        file.write("\n")

customers_df, customers_report = clean_customers(customers_df)
write_report("Customers Table Cleaning Report", customers_report, "w")    
customers_df.to_csv(
    "data/cleaned/customers.csv",
    index=False
)

def clean_products(df):

    df = df.copy()

    report = {}

    # Basic Profiling
    report["Total Rows Processed"] = len(df)
    report["Missing Values"] = df.isnull().sum().sum()
    report["Duplicate Rows"] = df.duplicated().sum()

    # Count Product Names with Leading/Trailing Spaces
    trimmed_product_names = (
        df["product_name"] !=
        df["product_name"].str.strip()
    ).sum()

    report["Trimmed Product Names"] = trimmed_product_names

    # Normalize product names
    df["product_name"] = (
        df["product_name"]
        .str.strip()
        .str.title()
    )

    # Remove Leading/Trailing Spaces
    df["category"] = df["category"].str.strip()
    df["subcategory"] = df["subcategory"].str.strip()

    # Validate Cost Price
    invalid_cost_price = df[
        df["cost_price"] <= 0
    ]

    report["Invalid Cost Price"] = len(invalid_cost_price)

    # Remove Invalid Cost Price Records
    rows_before = len(df)

    df = df[
        df["cost_price"] > 0
    ].copy()

    report["Rows Removed"] = rows_before - len(df)
    report["Rows Remaining"] = len(df)

    # print("\nProducts Table Cleaning Report:")
    # print("-" * 50)
    # for category, count in report.items():
    #     print(f"{category}: {count}")
    
    # print("\n\n\n")

    return df, report

products_df, product_report = clean_products(products_df)

write_report(
    "Products Table Cleaning Report",
    product_report,
    "a"
)

products_df.to_csv(
    "data/cleaned/products.csv",
    index=False
)

def clean_orders(df):

    df = df.copy()

    report = {}

    # Basic Profiling
    report["Total Rows Processed"] = len(df)
    report["Missing Values"] = df.isnull().sum().sum()
    report["Duplicate Rows"] = df.duplicated().sum()

    # Fix Date Format
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="mixed",
        dayfirst=True
    )

    total_removed = 0

    # Validate Order Status
    VALID_ORDER_STATUS = {
        "PLACED",
        "SHIPPED",
        "DELIVERED",
        "CANCELLED",
        "RETURNED"
    }

    invalid_status = df[
        ~df["status"].isin(VALID_ORDER_STATUS)
    ]

    report["Invalid Order Status"] = len(invalid_status)

    before = len(df)

    df = df[
        df["status"].isin(VALID_ORDER_STATUS)
    ].copy()

    total_removed += before - len(df)

    # Validate NULL Customer IDs
    null_customer_ids = df["customer_id"].isnull().sum()

    report["NULL Customer IDs"] = null_customer_ids

    before = len(df)

    df = df[
        df["customer_id"].notnull()
    ].copy()

    total_removed += before - len(df)

    # Final Summary
    report["Rows Removed"] = total_removed
    report["Rows Remaining"] = len(df)

    return df, report

orders_df, orders_report = clean_orders(orders_df)

write_report(
    "Orders Table Cleaning Report",
    orders_report,
    "a"
)
orders_df.to_csv(
    "data/cleaned/orders.csv",
    index=False
)

def check_referential_integrity(order_items_df, orders_df):

    invalid_order_items = order_items_df[
        ~order_items_df["order_id"].isin(
            orders_df["order_id"]
        )
    ]

    return invalid_order_items

def clean_order_items(order_items_df, orders_df):

    df = order_items_df.copy()

    report = {}

    # Basic Profiling
    report["Total Rows Processed"] = len(df)
    report["Missing Values"] = df.isnull().sum().sum()
    report["Duplicate Rows"] = df.duplicated().sum()

    total_removed = 0

    # Referential Integrity
    invalid_order_items = check_referential_integrity(
        df,
        orders_df
    )

    report["Order Items with Invalid Order IDs"] = len(invalid_order_items)

    before = len(df)

    df = df[
        df["order_id"].isin(
            orders_df["order_id"]
        )
    ].copy()

    total_removed += before - len(df)

    # Invalid Quantity
    invalid_quantity = df[
        df["quantity"] <= 0
    ]

    report["Invalid Quantity"] = len(invalid_quantity)

    before = len(df)

    df = df[
        df["quantity"] > 0
    ].copy()

    total_removed += before - len(df)

    # Final Summary
    report["Total Invalid Rows Removed"] = total_removed
    report["Rows Remaining"] = len(df)

    # print("\nOrder Items Table Cleaning Report:")
    # print("-" * 50)
    # for category, count in report.items():
    #     print(f"{category}: {count}")
    
    # print("\n\n\n")

    return df, report

invalid_order_items = check_referential_integrity(
    order_items_df,
    orders_df
)


print("\nOrder Items Referencing Non-Existent Orders")
print("-------------------------------------------")

if invalid_order_items.empty:
    print("No referential integrity violations found.")
else:
    print(invalid_order_items)


order_items_df, order_items_report = clean_order_items(order_items_df, orders_df)

write_report(
    "Order Items Table Cleaning Report",
    order_items_report,
    "a"
)
    
order_items_df.to_csv(
    "data/cleaned/order_items.csv",
    index=False
)
