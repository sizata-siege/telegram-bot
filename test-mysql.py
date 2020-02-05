import mysql.connector

con = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "test"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM table1")
results = cursor.fetchall()

print(results)