import sqlite3

db = sqlite3.connect("test.db")
print('ok')

cursor = db.cursor()

action = """create table user(
    code INTEGER,
    name TEXT(20)
)"""
cursor.execute(action)
db.commit()
print("Ok!!!")
db.close()