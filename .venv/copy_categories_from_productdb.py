import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="new_bikecorp_db"
)
cursor = conn.cursor()

cursor.execute("SELECT category_id, category_name FROM productdb.categories")
rows = cursor.fetchall()

insert_query = """
    INSERT INTO categories (category_id, category_name)
    VALUES (%s, %s)
"""

for row in rows:
    cursor.execute(insert_query, row)

conn.commit()
cursor.close()
conn.close()

print("Kategorier indsat i new_bikecorp_db.")
