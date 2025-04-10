import csv
import mysql.connector

with open(r"C:\Users\spac-27\Desktop\Uge 6 kode\data_csv\staffs.csv", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    staffs_data = list(reader)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()

for row in staffs_data:
    cursor.execute("""
        INSERT INTO staffs (
            store_name, manager_id, street
        ) VALUES (%s, %s, %s)
    """, (
        row["store_name"],
        row["manager_id"],
        row["street"]
    ))

conn.commit()
print(f"Indsat {len(staffs_data)} rækker i 'staffs'")
cursor.close()
conn.close()
