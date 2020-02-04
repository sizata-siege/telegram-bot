import sqlite3

con = sqlite3.connect('E:/Faradars.org/faradars.db')
c=con.cursor()

com="update user set age=30 where code=2"
try:
    c.execute(com)
    con.commit()
except:
    print('error')
    con.rollback()

con.close()