import mysql.connector

# Instantiate connector.
connector = mysql.connector.connect(
    host="localhost",
    user="root",  # change if necessary, but it shouldn't be.
    password="Velkommen25"  # set password.
)



# Open a cursor.
try:
    cursor = connector.cursor(dictionary=True)
    cursor.execute("CREATE USER 'curseist'@'localhost' IDENTIFIED BY 'curseword'")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'curseist'@'%'")
    cursor.execute("CREATE DATABASE ProductDB")
    connector.commit()
except Exception as e:
    print(f"commit failed with: {e}")
    exit
# Close cursor
cursor.close()

print("fino dino!")
