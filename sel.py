import sqlite3

con = sqlite3.connect('E:/Faradars.org/faradars.db')
c=con.cursor()

com="select * from user where name1='ali'"
try:
    c.execute(com)
    r=c.fetchall()
    for row in r:
        print(row)
except:
    print('error')

con.close()