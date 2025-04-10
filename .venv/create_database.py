import mysql.connector

connector = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="Velkommen25"  
)



try:
    cursor = connector.cursor(dictionary=True)
    cursor.execute("CREATE DATABASE new_bikecorp_db")
    connector.commit()
except Exception as e:
    print(f"commit failed with: {e}")
    exit

cursor.close()

print("fino dino!")