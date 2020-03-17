#IN THE NAME OF GOD
import pymysql

connector = pymysql.connect('localhost', 'root', '', 'user')
cursor = connector.cursor()

def Add():
    name = input("Enter the name : ")
    size = input("Enter the size : ")
    code = input("Enter the code : ")
    string = input("Enter string : ")
    add = "insert into test values({}, {}, {}, {})".format(name, size, code, string)
    #try:
    cursor.execute(add)
    cursor.commit()
    print("Added Successfully !!!")
    #except:
        #connector.rollback()
        #print("Error !")

while True:    
    Add()