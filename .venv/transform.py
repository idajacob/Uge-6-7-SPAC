import requests
import mysql.connector

response = requests.get("http://localhost:8000/customers")
customers_data = response.json()

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
            customer_id, first_name, last_name, phone,
            email, street, city, state, zip_code
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(customer["customer_id"]),
        customer["first_name"],
        customer["last_name"],
        customer["phone"],
        customer["email"],
        customer["street"],
        customer["city"],
        customer["state"],
        int(customer["zip_code"])
    ))

conn.commit()
print("Data fra API indsat i 'customers'.")
cursor.close()
conn.close()
