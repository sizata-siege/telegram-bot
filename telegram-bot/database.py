# This is the connector module that uses 3 way to connect to 3 type of databases
# Create some tables connected to each other using primary key and foreign key
# Tables : bot_users_data , bot_users_scores , bot_admins
# What is the best way to use database and the connection ? connect once or connect each time ?
# What is the best way to use cursor ? define a cursor once or define each time ?
# Use a timer that if the connection is not used after 1 min, close the connection and if not, wait
# How to do that ???
# define a timer and start it when connected to database and reset it each time a query runs (restart timer)
# and when the timer finishes ( reaches ), disconnect from database specially mysql
# I think not really important for sqlite. The time out is for example 5 min or 10 min

# ------------------------------ Modules ------------------------------ #
# python3 -m pip install mysql-connector or something else
import sqlite3
import mysql.connector as mysql_connector
from threading import Timer
# ------------------------------ Defaults ------------------------------ #
default_sqlite_database = "database/telegram_bot.db"
# ------------------------------ SQLite ------------------------------ #
class Sqlite_db:
    def __init__(self, database=default_sqlite_database):
        self.database = database
        self.status = 'disconneted'
        self.auto_disconnect = True
        self.adt = 60
    
    def __str__(self):
        return self.database + self.status

    def connect(self):
        self.sqlite = sqlite3.connect(self.database, check_same_thread=False)
        self.status = 'connected'
        if self.auto_disconnect:
            self.set_timer(self.adt)
            # print('timer set in connect')
        print('connected to sqlite database')

    def cursor(self):
        return self.sqlite.cursor()

    def disconnect(self):
        self.sqlite.close()
        self.timer.cancel()
        self.status = 'disconnected'
        print('disconnected from sqlite database')

    def reset_timer(self):
        self.timer.cancel()
        self.set_timer(self.adt)
        # print('timer reset')

    def set_timer(self, t):
        self.timer = Timer(t, self.disconnect)
        self.timer.start()
        # print('timer set in set_timer')


# ------------------------------ MySql ------------------------------ #
class Mysql_db:
    def __init__(self):
        self.status = 0 # disconnected
        self.auto_disconnect = True
        self.adt = 60
        # print('created Mysql_db object')
    
    def __str__(self):
        return self.status

    def connect(self):
        if not self.status:
            self.mysql = mysql_connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="activity_monitoring_bot"
            )
            self.status = 1 # connected
            if self.auto_disconnect:
                self.set_timer(self.adt)
                # print('timer set in connect')
            print('connected to mysql database')
        else:
            print('Prevented reconnection')
    
    def cursor(self):
        return self.mysql.cursor()

    def disconnect(self):
        self.mysql.close()
        self.timer.cancel()
        self.status = 0 # disconnected
        print('disconnected from mysql database')
        
    def reset_timer(self):
        self.timer.cancel()
        self.set_timer(self.adt)
        # print('timer reset')

    def set_timer(self, t):
        self.timer = Timer(t, self.disconnect)
        self.timer.start()
        # print('timer set in set_timer')

    def create_db(self, name):
        create_db = "create database %s" % name
        self.cursor().execute(create_db)

    # ------------------------------ Common functions ------------------------------ #
    def show_all_databases(self):
        self.connect()
        show_databases = "show databases"
        cursor = self.cursor()
        cursor.execute(show_databases)
        return cursor.fetchall()

    def create_bot_users_table(self):
        self.connect()
        create_bot_users = """
        create table bot_users(
            chat_id int not null,
            username varchar(32),
            groups varchar(200),
            first_name varchar(64),
            last_name varchar(64),
        )
        """
        
            
""" default_mysql = mysql_connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="activity_monitoring_bot"
) """
# ------------------------------ other databases ------------------------------ #



# ------------------------------ functions ------------------------------ #
def create_db(name):
    create_db = "create database %s" % name


def create_bot_users():
    create_bot_users = """
    create table bot_users(
    chat_id integer primary key
    """


def show_all_databases(cursor):
    show_databases = "show databases"
    cursor.execute(show_databases)
    return cursor.fetchall()





# db1 = Sqlite_db()
# db1.connect()
# db1.disconnect()

db2 = Mysql_db()
db2.connect()

# print(show_all_databases(db2.cursor()))
print(db2.show_all_databases())
# db2.create_db('test4')

db2.disconnect()
input()