import pandas as pd
import mysql.connector
import requests
import json 


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return pd.DataFrame(json.loads(response.text))
        except Exception as e:
            print(f"Fejl ved parsing af data fra {url}: {e}")
            return pd.DataFrame()
    else:
        print(f"Fejl ved hentning fra {url}: {response.status_code}")
        return pd.DataFrame()


customers_df = fetch_data("http://localhost:8000/customers")
orders_df = fetch_data("http://localhost:8000/orders")
order_items_df = fetch_data("http://localhost:8000/order_items")


if 'store' in orders_df.columns:
    orders_df = orders_df.rename(columns={"store": "store_name"})

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25", 
    database="new_bikecorp_db"
)
cursor = conn.cursor()

for _, row in customers_df.iterrows():
    cursor.execute("""
        INSERT INTO customers (customer_id, zip_code, state, city, street, first_name, last_name, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['customer_id'], row['zip_code'], row['state'], row['city'],
        row['street'], row['first_name'], row['last_name'], row['email']
    ))


for _, row in orders_df.iterrows():
    cursor.execute("""
        INSERT INTO orders (order_id, customer_id, order_date, shipped_date, store_name)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row['order_id'], row['customer_id'], row['order_date'],
        row['shipped_date'], row['store_name']
    ))


for _, row in order_items_df.iterrows():
    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, quantity, list_price)
        VALUES (%s, %s, %s, %s)
    """, (
        row['order_id'], row['product_id'], row['quantity'], row['list_price']
    ))


conn.commit()
cursor.close()
conn.close()

print("API-data er hentet, transformeret og indlæst.")
