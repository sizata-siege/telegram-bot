import pymysql

con=pymysql.connect('localhost','root','','faradars')
c=con.cursor()
com="select * from user where name ='ali'"
try:
    c.execute(com)
    r=c.fetchall()
    for row in r:
        print(row)
except:
    print('error')

con.close()