import sqlite3

con = sqlite3.connect('E:/Faradars.org/faradars.db')
c=con.cursor()

com="""create table user(
         code INTEGER PRIMARY key,
         name1 Text(20),
         family Text(30),
         age INTEGER)"""
try:
    c.execute(com)
    con.commit()
except:
    print('error')
    con.rollback()

con.close()