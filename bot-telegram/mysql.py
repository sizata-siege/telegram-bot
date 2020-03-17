import pymysql

connector = pymysql.connect('remotemysql.com','zZg4TSbkYB','r9F4W0h329','zZg4TSbkYB')
print("Connected Successfully !!!")

# cursor
c = connector.cursor()

#command
com = """create table test(
            code int PRIMARY KEY ,
            name varchar(20),
            age int(3))"""
add = "insert into bot_users values(1, 'test', 'test', 'username',,,,,,,,,,,)"
add_test = "insert into test values(1, 'test', '')"
c.execute(add_test)
connector.commit()

connector.close()

#----------USERS DATABASE----------#
#ID										|id
#firstname								|fname
#last name								|lname
#username								|username
#telegram first name					|tfname
#telegram last name						|tln
#post / job								|post
#chatid									|chatid
#activity database link					|adb
#score									|score
#number of forwarded messages			|nofm
#number of sent activities				|nosa
#number of sent messages in group		|nosm
#number of sent formal notifications	|nosn
#number of replied messages				|norm
