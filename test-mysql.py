import mysql.connector

con = mysql.connector.connect(
    user = "xoEe4hNkKr",
    password = "dxFTpB2adi",
    host = "remotemysql.com",
    database = "xoEe4hNkKr"
)

cursor = con.cursor()

def add(name, number):
    add = "insert into bot_users VALUES ('%s', %s, %s)" % (name, number, number)
    cursor.execute(add)
    con.commit()
    print("Added!")

def update(name):
    select = "select * from bot_users where username = '%s'" % name
    cursor.execute(select)
    results = cursor.fetchone()
    print(results)
    n = int(results[1]) + 1
    print(n)
    update = "update bot_users set nosm = %s where username = '%s'" % (n, name)
    cursor.execute(update)
    con.commit()
    print("Updated!")

while False:    
    name = input("Enter the name : ")
    number = input("Enter the number : ")
    add(name, number)
name = input("Enetr the name : ")
update(name)

query = cursor.execute("SELECT * FROM bot_users")
results = cursor.fetchall()

print(results)
con.close()