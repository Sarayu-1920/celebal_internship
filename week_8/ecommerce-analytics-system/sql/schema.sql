-- Drop Existing Tables
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;


-- Customers Table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT NOT NULL,
    registration_date TEXT,
    customer_type TEXT CHECK (
        customer_type IN ('REGULAR', 'PREMIUM', 'VIP')
    )
);


-- Products Table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    subcategory TEXT,
    cost_price REAL
);


-- Orders Table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    status TEXT CHECK (
        status IN (
            'PLACED',
            'SHIPPED',
            'DELIVERED',
            'CANCELLED',
            'RETURNED'
        )
    ),
    region_code TEXT,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- Order Items Table
CREATE TABLE order_items (
    item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    discount_percent REAL,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);