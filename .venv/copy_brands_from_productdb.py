import mysql.connector

source_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="productdb"
)
target_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)

source_cursor = source_conn.cursor(dictionary=True)
target_cursor = target_conn.cursor()

source_cursor.execute("SELECT brand_id, brand_name FROM brands")
brands = source_cursor.fetchall()

for row in brands:
    target_cursor.execute("""
        INSERT INTO brands (
            brand_id, brand_name
        ) VALUES (%s, %s)
    """, (
        row["brand_id"],
        row["brand_name"]
    ))

target_conn.commit()
print(f"Kopieret {len(brands)} brands.")
source_cursor.close()
target_cursor.close()
source_conn.close()
target_conn.close()
