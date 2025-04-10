import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25", 
    database="new_bikecorp_db"
)
cursor = conn.cursor()

cursor.execute("""
    SELECT 
        product_id,
        product_name,
        brand_id,
        category_id,
        model_year,
        list_price
    FROM productdb.products
""")
rows = cursor.fetchall()

insert_query = """
    INSERT INTO products (
        product_id, product_name, brand_id, category_id, model_year, list_price
    ) VALUES (%s, %s, %s, %s, %s, %s)
"""

for row in rows:
    cursor.execute(insert_query, row)

conn.commit()
cursor.close()
conn.close()

print("Produkter indsat i new_bikecorp_db.")
