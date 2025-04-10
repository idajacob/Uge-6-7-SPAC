import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS stores;")

cursor.execute("""
CREATE TABLE stores (
    store_name TEXT,
    state TEXT,
    zip_code INT,
    city TEXT,
    street TEXT
)
""")

conn.commit()
print("Stores-tabellen er oprettet.")
cursor.close()
conn.close()
