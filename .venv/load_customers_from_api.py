import requests
import mysql.connector
import json


response = requests.get("http://127.0.0.1:8000/customers")
customers_data = json.loads(response.json()) 

print(type(customers_data))       
print(type(customers_data[0]))    


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()


for customer in customers_data:
    cursor.execute("""
        INSERT INTO customers (
            customer_id, zip_code, state, city,
            first_name, last_name, email
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        int(customer["customer_id"]),
        int(customer["zip_code"]),
        customer["state"],
        customer["city"],
        customer["first_name"],
        customer["last_name"],
        customer["email"]
    ))

conn.commit()
print(f"{len(customers_data)} kunder indsat i 'customers'-tabellen.")
cursor.close()
conn.close()
