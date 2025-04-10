
import requests
import json
import mysql.connector

response = requests.get("http://localhost:8000/order_items")
order_items_data = json.loads(json.loads(response.text))

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()

for item in order_items_data:
    cursor.execute("""
        INSERT INTO order_items (
            order_id, product_id, quantity, list_price
        ) VALUES (%s, %s, %s, %s)
    """, (
        int(item["order_id"]),
        int(item["product_id"]),
        int(item["quantity"]),
        float(item["list_price"])
    ))

conn.commit()
print(f"Indsat {len(order_items_data)} order items.")
cursor.close()
conn.close()
