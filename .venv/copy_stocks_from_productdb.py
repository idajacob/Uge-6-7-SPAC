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

source_cursor.execute("SELECT store_name, product_id, quantity FROM stocks")
stocks = source_cursor.fetchall()

for row in stocks:
    target_cursor.execute("""
        INSERT INTO stocks (
            store_name, product_id, quantity
        ) VALUES (%s, %s, %s)
    """, (
        row["store_name"],
        row["product_id"],
        row["quantity"]
    ))

target_conn.commit()
print(f"Kopieret {len(stocks)} stock-rækker.")
source_cursor.close()
target_cursor.close()
source_conn.close()
target_conn.close()
