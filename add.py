import sqlite3

con = sqlite3.connect('E:/Faradars.org/faradars.db')
c=con.cursor()

com="insert into user VALUES (2,'ali','ahmadi',25)"
try:
    c.execute(com)
    con.commit()
except:
    print('error')
    con.rollback()

con.close()