import pymysql

con=pymysql.connect('localhost','root','','faradars')
c=con.cursor()
com="insert into user values(2,'ali','ahmadi',25)"
try:
    c.execute(com)
    con.commit()
except:
    print('error')
    con.rollback()

con.close()