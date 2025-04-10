import csv
import mysql.connector

with open(r"C:\Users\spac-27\Desktop\Uge 6 kode\data_csv\stores.csv", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    stores_data = list(reader)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()

for row in stores_data:
    cursor.execute("""
        INSERT INTO stores (
            store_name, state, zip_code, city, street
        ) VALUES (%s, %s, %s, %s, %s)
    """, (
        row["name"],       
        row["state"],
        int(row["zip_code"]),
        row["city"],
        row["street"]
    ))

conn.commit()
print(f"Indsat {len(stores_data)} butikker.")
cursor.close()
conn.close()
