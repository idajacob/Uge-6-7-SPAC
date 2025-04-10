import requests
import mysql.connector
import json


response = requests.get("http://127.0.0.1:8000/orders")
orders_data = json.loads(response.json())  

print(type(orders_data))       
print(type(orders_data[0]))    
print(orders_data[0])          


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()


for order in orders_data:
    cursor.execute("""
        INSERT INTO orders (
            order_id, customer_id, order_date, shipped_date, store
        ) VALUES (%s, %s, %s, %s, %s)
    """, (
        int(order["order_id"]),
        int(order["customer_id"]),
        order["order_date"],
        order["shipped_date"],
        order["store"]
    ))

conn.commit()
print(f"{len(orders_data)} ordrer indsat.")
cursor.close()
conn.close()

import requests
import pandas as pd
import mysql.connector
import json

response = requests.get("http://127.0.0.1:8000/orders")
orders_data = json.loads(response.json())

orders_df = pd.DataFrame(orders_data)

if 'store' in orders_df.columns:
    orders_df = orders_df.rename(columns={"store": "store_name"})

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()

for _, order in orders_df.iterrows():
    cursor.execute("""
        INSERT INTO orders (
            order_id, customer_id, order_date, shipped_date, store_name
        ) VALUES (%s, %s, %s, %s, %s)
    """, (
        int(order["order_id"]),
        int(order["customer_id"]),
        order["order_date"],
        order["shipped_date"],
        order["store_name"]
    ))

conn.commit()
print(f"{len(orders_df)} ordrer indsat.")
cursor.close()
conn.close()
