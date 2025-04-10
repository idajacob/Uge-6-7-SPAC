import requests
import pandas as pd
import json
import mysql.connector

url = "http://192.168.20.171:8000/orders"
auth = ('curseit', 'curseword')

response = requests.get(url, auth=auth)
raw_text = response.text

first_pass = json.loads(raw_text)
data = json.loads(first_pass) if isinstance(first_pass, str) else first_pass

df = pd.DataFrame(data)
print("Forbindelse oprettet")
print(df.head())

dato_kolonner = ["order_date", "required_date", "shipped_date"]
for kol in dato_kolonner:
    df[kol] = pd.to_datetime(df[kol], format="%d/%m/%Y", errors='coerce')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",  
    database="productdb"     
)
cursor = conn.cursor()

for order in df.itertuples(index=False):
    cursor.execute("""
        INSERT INTO orders (
            order_id, customer_id, order_status, order_date,
            required_date, shipped_date, store, staff_name
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(order.order_id),
        int(order.customer_id),
        order.order_status,
        order.order_date.date() if pd.notnull(order.order_date) else None,
        order.required_date.date() if pd.notnull(order.required_date) else None,
        order.shipped_date.date() if pd.notnull(order.shipped_date) else None,
        order.store,
        order.staff_name
    ))

conn.commit()
print(f"{len(df)} ordrer indsat")
cursor.close()
conn.close()
