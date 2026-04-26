import json
import time
import random
from datetime import datetime
import os

output_folder = "../../data/raw/"

products = [
    ("iPhone", "Electronics", 999),
    ("Laptop", "Electronics", 1200),
    ("Shoes", "Fashion", 120),
    ("Watch", "Accessories", 250),
    ("Headphones", "Electronics", 199)
]

os.makedirs(output_folder, exist_ok=True)

order_id = 1000

while True:
    order = {
        "order_id": order_id,
        "customer_id": random.randint(1000, 1100),
        "product": random.choice(products)[0],
        "category": random.choice(products)[1],
        "price": random.choice(products)[2],
        "quantity": random.randint(1, 3),
        "order_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    file_name = f"{output_folder}/order_{order_id}.json"

    with open(file_name, "w") as f:
        json.dump(order, f)

    print(f"Generated {file_name}")

    order_id += 1
    time.sleep(2)
