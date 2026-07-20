from faker import Faker
import random
import pandas as pd

fake = Faker()

NUM_CUSTOMERS = 500

CUSTOMER_TYPES = ["REGULAR", "PREMIUM", "VIP"]


def generate_customers():
    customers = []

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        customers.append({
            "customer_id": customer_id,
            "customer_name": fake.name(),
            "email": fake.email(),
            "registration_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            ),
            "customer_type": random.choice(CUSTOMER_TYPES)
        })

    # Introduce 2% invalid email addresses
    invalid_email_count = int(NUM_CUSTOMERS * 0.02)

    invalid_indexes = random.sample(
        range(len(customers)),
        invalid_email_count
    )

    for index in invalid_indexes:

        email = customers[index]["email"]

        if random.choice([True, False]):
            # Remove '@'
            customers[index]["email"] = email.replace("@", "")
        else:
            # Remove domain
            customers[index]["email"] = email.split("@")[0]


    return pd.DataFrame(customers)


customers_df = generate_customers()

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

print("customers.csv generated successfully")
print(customers_df.head())


NUM_PRODUCTS = 500


CATEGORIES = {
    "Electronics": [
        "Mobile",
        "Laptop",
        "Accessories"
    ],
    "Clothing": [
        "Men",
        "Women",
        "Kids"
    ],
    "Home": [
        "Kitchen",
        "Furniture",
        "Decor"
    ],
    "Books": [
        "Fiction",
        "Education",
        "Comics"
    ]
}

def generate_products():

    products = []

    for product_id in range(1, NUM_PRODUCTS + 1):

        category = random.choice(list(CATEGORIES.keys()))

        subcategory = random.choice(CATEGORIES[category])

        product_name = f"{fake.word().title()} {subcategory}"

        # Introduce inconsistent product names
        if random.random() < 0.05:

            product_name = random.choice([
                product_name.lower(),
                product_name.upper(),
                f"  {product_name}  "
            ])

        products.append({

            "product_id": product_id,

            "product_name": product_name,

            "category": category,

            "subcategory": subcategory,

            "cost_price": round(random.uniform(100, 5000), 2)

        })

    return pd.DataFrame(products)

products_df = generate_products()

product_price_map = dict(
    zip(products_df["product_id"], products_df["cost_price"])
)

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

print(products_df.head())

NUM_ORDERS = 500

ORDER_STATUS = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

REGIONS = ["North", "South", "East", "West"]

def generate_orders():

    orders = []

    for order_id in range(1, NUM_ORDERS + 1):

        customer_id = random.randint(1, NUM_CUSTOMERS)

        order_date = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        status = random.choice(ORDER_STATUS)

        region_code = random.choice(REGIONS)


        # 5% NULL customer_id
        if random.random() < 0.05:
            customer_id = None

        # Some wrong date formats
        if random.random() < 0.05:
            order_date = order_date.strftime("%d-%m-%Y %H:%M:%S")
        else:
            order_date = order_date.strftime("%Y-%m-%d %H:%M:%S")

        orders.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date,
            "status": status,
            "region_code": region_code
        })

    return pd.DataFrame(orders)

orders_df = generate_orders()

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print(orders_df.head())

NUM_ITEMS = 500

def generate_order_items():

    order_items=[];

    for index in range(1,NUM_ITEMS+1):
        
        random_product_id = random.randint(1, NUM_PRODUCTS)

        quantity = random.randint(1,10)

        if random.random()<0.03:
            quantity = random.randint(-200,-1)

        order_items.append({
            "item_id": index,
            "order_id" : random.randint(1,NUM_ORDERS),

            "product_id" : random_product_id,
            "quantity" : quantity,
            "unit_price": product_price_map[
                random_product_id
            ],
            "discount_percent" : round(random.uniform(0,100),2)

        })

    return pd.DataFrame(order_items)

order_items_df = generate_order_items()

order_items_df.to_csv(
    "data/raw/order_items.csv",
    index = False
)

print(order_items_df.head())