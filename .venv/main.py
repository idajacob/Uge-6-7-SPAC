print("hello")

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="productdb"
)

print("hep hey")

cursor = conn.cursor()

cursor.execute("SELECT * FROM categories LIMIT 5")

for row in cursor.fetchall():
    print(row)

conn.close()