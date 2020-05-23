# This is the connector module that uses 3 way to connect to 3 type of databases
# Create some tables connected to each other using primary key and foreign key
# Tables : bot_users_data , bot_users_scores , bot_admins , bot_groups
# What is the best way to use database and the connection ? connect once or connect each time ?
# What is the best way to use cursor ? define a cursor once or define each time ?
# Use a timer that if the connection is not used after 1 min, close the connection and if not, wait
# How to do that ???
# define a timer and start it when connected to database and reset it each time a query runs (restart timer)
# and when the timer finishes ( reaches ), disconnect from database specially mysql
# I think not really important for sqlite. The time out is for example 5 min or 10 min
# Add logging or use a logger to log everything in a file or something
# The third method is sending the requests to the php server and get the result
# for the hard situations :)

# ------------------------------ Modules ------------------------------ #
# python3 -m pip install mysql-connector or something else
from config import default_mysql_database, default_mysql_adt, default_sqlite_adt, default_sqlite_database
import sqlite3
import mysql.connector as mysql_connector
from threading import Timer
import logging
# ------------------------------ Logger ------------------------------ #
# db_logger = logging.getLogger('DataBase').addHandler(logging.NullHandler())  # prevent display
db_logger = logging.getLogger('DataBase')  # create logger
# db_logger.setLevel(logging.DEBUG)
# db_console_handler = logging.StreamHandler()  # create console handler
# db_console_handler.setLevel(logging.DEBUG)
# db_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')  # create formatter
# db_console_handler.setFormatter(db_formatter)  # add formatter to console_handler
# db_logger.addHandler(db_console_handler)  # add console_handler to logger
# ------------------------------ SQLite ------------------------------ #
class SqliteDB:
    def __init__(self, database=default_sqlite_database):
        self.database = database
        self.status = 'disconnected'
        self.auto_disconnect = True
        self.adt = default_sqlite_adt
        self.logger = logging.getLogger('DataBase.Sqlite')
        self.logger.info('Created SqliteDB object')

    def __str__(self):
        self.logger.debug('__str__ called for %s' % self.database)
        return self.database + self.status

    def connect(self):
        self.sqlite = sqlite3.connect(self.database, check_same_thread=False)
        self.status = 'connected'
        if self.auto_disconnect:
            self.set_timer(self.adt)
            self.logger.debug('timer was set in connect')
        self.logger.debug('connected to sqlite database')

    def cursor(self):
        self.logger.debug('used cursor')
        try:
            return self.sqlite.cursor()
        except Exception as e:
            self.logger.error('failed to get cursor %s' % e)

    def disconnect(self):
        self.sqlite.close()
        self.timer.cancel()
        self.status = 'disconnected'
        self.logger.debug('disconnected from sqlite database')

    def reset_timer(self):
        self.timer.cancel()
        self.set_timer(self.adt)
        self.logger.debug('timer reset')

    def set_timer(self, t):
        self.timer = Timer(t, self.disconnect)
        self.timer.start()
        self.logger.debug('timer set in set_timer')

    # ------------------------------ Common functions ------------------------------ #
    def show_all_tables(self):
        self.connect()
        self.logger.debug('show_all_tables was called')
        show_tables = "show tables"
        cursor = self.cursor()
        try:
            cursor.execute(show_tables)
            self.logger.debug('returned all tables')
            return cursor.fetchall()
        except Exception as e:
            self.logger.error('Failed to show tables %s' % e)

    def create_bot_users_data_table(self):
        self.connect()
        self.logger.debug('create bot users data table was called')
        create_bot_users_data = """
        create table bot_users_data(
            chat_id int not null primary key,
            username varchar(32),
            group_chat_id int references bot_groups(group_chat_id),
            first_name varchar(64),
            last_name varchar(64)
        )"""
        cursor = self.cursor()
        try:
            cursor.execute(create_bot_users_data)
            self.logger.info('Created bot_users_data_table')
        except Exception as e:
            self.logger.error('failed to create bot users data table %s' % e)

    def create_bot_users_scores_table(self):
        self.connect()
        create_bot_users_scores = """
        create table bot_users_scores(
            chat_id int not null primary key references bot_users_data(chat_id),
            score int,
            nosm int,
            nofm int,
            norm int,
            nosw int,
            nosv int,
            nosa int,
            nosp int
        )"""
        cursor = self.cursor()
        try:
            cursor.execute(create_bot_users_scores)
            self.logger.info('Created bot_users_scores_table')
        except Exception as e:
            self.logger.error('failed to create bot users scores table %s' % e)

    def create_bot_groups_table(self):
        self.connect()
        create_bot_groups = """
        create table bot_groups(
            group_name varchar(32),
            group_owner varchar(32),
            group_chat_id int,

            primary key(group_chat_id)
        )
        """
        cursor = self.cursor()
        try:
            cursor.execute(create_bot_groups)
            self.logger.info('Created bot_groups_table')
        except Exception as e:
            self.logger.error('failed to create bot groups table %s' % e)

    def add_user(self, chat_id, username, group_chat_id, first_name, last_name):
        self.connect()
        self.logger.debug('new user %s is about to be added to database' % username)
        insert_user = "insert into bot_users_data (chat_id, username, group_chat_id, first_name, last_name) values (%s, %s, %s, %s, %s)"
        val = (chat_id, username, group_chat_id, first_name, last_name)
        cursor = self.cursor()
        try:
            cursor.execute(insert_user, val)
            self.logger.info('Added user %s to database' % username)
        except Exception as e:
            self.logger.error('failed to add user %s' % e)

    def check_username(self, username):
        self.logger.debug('used check username')
        self.connect()
        select = "select * from bot_users_data where username = '%s'" % username
        cursor = self.cursor()
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got username')
            return result
        except Exception as e:
            self.logger.info("User is not in database! : %s" % e)
            return 0

    def check_chat_id(self, chat_id):
        self.logger.debug('used check chat_id')
        self.connect()
        select = "select * from bot_users_data where chat_id = '%s'" % chat_id
        cursor = self.cursor()
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got chat_id')
            return result
        except Exception as e:
            self.logger.info("Chat_id %s is not in database! : %s" % (chat_id, e))
            return 0

    def add_score(self, chat_id, score):
        self.logger.debug('used add score')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            s = result[1]
            s += score
            update = "update bot_users_scores set score = '%s' where chat_id = '%s'" % (s, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s score to %s" % (score, chat_id))
        except Exception as e:
            self.logger.error("Failed to add score! : %s" % e)
            self.sqlite.rollback()

    def nosm_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosm inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosm = result[2]
            nosm += n
            update = "update bot_users_scores set nosm = '%s' where chat_id = '%s'" % (nosm, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s messages to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosm! : %s" % e)
            self.sqlite.rollback()

    def nofm_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nofm inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nofm = result[3]
            nofm += n
            update = "update bot_users_scores set nofm = '%s' where chat_id = '%s'" % (nofm, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s forward to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nofm! : %s" % e)
            self.sqlite.rollback()

    def norm_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used norm inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            norm = result[4]
            norm += n
            update = "update bot_users_scores set norm = '%s' where chat_id = '%s'" % (norm, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s reply to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase norm! : %s" % e)
            self.sqlite.rollback()

    def nosw_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosw inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosw = result[5]
            nosw += n
            update = "update bot_users_scores set nosw = '%s' where chat_id = '%s'" % (nosw, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s words to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosw! : %s" % e)
            self.sqlite.rollback()

    def nosv_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosv inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosv = result[6]
            nosv += n
            update = "update bot_users_scores set nosv = '%s' where chat_id = '%s'" % (nosv, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s voice to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosv! : %s" % e)
            self.sqlite.rollback()

    def nosa_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosa inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosa = result[7]
            nosa += n
            update = "update bot_users_scores set nosa = '%s' where chat_id = '%s'" % (nosa, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s activitie to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosa! : %s" % e)
            self.sqlite.rollback()

    def nosp_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosp inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosp = result[8]
            nosp += n
            update = "update bot_users_scores set nosp = '%s' where chat_id = '%s'" % (nosp, chat_id)
            cursor.execute(update)
            self.sqlite.commit()
            self.logger.info("Added %s project to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosp! : %s" % e)
            self.sqlite.rollback()

    def get_user(self, chat_id=None, username=None):
        self.logger.debug('used get user')
        self.connect()
        cursor = self.cursor()
        if chat_id:
            try:
                select = "select * from bot_users_data where chat_id = '%s'" % chat_id
                cursor.execute(select)
                result = cursor.fetchone()
                self.logger.debug('got user')
                return result
            except Exception as e:
                self.logger.error("Failed to get user information %s %s" % (chat_id, e))
        elif username:
            try:
                get_chat_id = "select * from bot_users_data where username = '%s'" % username
                cursor.execute(get_chat_id)
                result = cursor.fetchone()
                chat_id = result[0]
                try:
                    select = "select * from bot_users_data where chat_id = '%s'" % chat_id
                    cursor.execute(select)
                    result = cursor.fetchone()
                    self.logger.debug('got user')
                    return result
                except Exception as e:
                    self.logger.error("Failed to get user information %s : %s" % (chat_id, e))
            except Exception as e:
                self.logger.error("Failed to get chat id! : %s" % e)

    def get_chat_id(self, username):
        self.logger.debug('used get chat_id')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_data where username = '%s'" % username
        try:
            cursor.execute(select)
            user = cursor.fetchone()
            chat_id = user[0]
            self.logger.debug("got chat_id")
            return chat_id
        except Exception as e:
            self.logger.error("Failed to get chat_id : %s" % e)

    def calculate_rank(self, chat_id):
        self.logger.debug('used calculate rank')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores order by score desc"  # should I add ` ?
        u = self.get_user(chat_id)  # to get user
        user_group = u[2]  # to get user's group
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            rank = 0
            for result in results:
                tmp_chat_id = result[0]
                user = self.get_user(tmp_chat_id)
                group = user[2]
                if group == user_group:
                    rank += 1
                    if result[0] == chat_id:
                        return rank
        except Exception as e:
            self.logger.error("Failed to calculate %s rank : %s" % (chat_id, e))
            return 0  # should take care when using this function that if returned 0 means failed

    def get_score(self, chat_id):
        self.logger.debug('used get score')
        self.connect()
        cursor = self.cursor()
        try:
            select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got score')
            return result
        except Exception as e:
            self.logger.error("Failed to get user information %s : %s" % (chat_id, e))

# ------------------------------ MySql ------------------------------ #
class MysqlDB:
    def __init__(self):
        self.status = 0  # disconnected
        self.auto_disconnect = True
        self.adt = default_mysql_adt  # auto disconnect time
        self.logger = logging.getLogger('DataBase.Mysql')
        self.logger.info('Created MysqlDB object')

    def __str__(self):
        self.logger.debug('__str__ was called for %s' % self)  # what will print in the console for self ?
        return self.status

    def connect(self):
        if not self.status:
            self.mysql = mysql_connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="activity_monitoring_bot"
            )
            self.status = 1  # connected
            if self.auto_disconnect:
                self.set_timer(self.adt)
                # print('timer set in connect')
            self.logger.debug('connected to mysql database')
        else:
            self.logger.debug('Prevented reconnection')

    def cursor(self):
        self.logger.debug('cursor used')
        try:
            return self.mysql.cursor()
        except Exception as e:
            self.logger.error('failed to get cursor %s' % e)

    def disconnect(self):
        self.mysql.close()
        self.timer.cancel()
        self.status = 0  # disconnected
        self.logger.debug('disconnected from mysql database')

    def reset_timer(self):
        self.timer.cancel()
        self.set_timer(self.adt)
        self.logger.debug('timer reset')

    def set_timer(self, t):
        self.timer = Timer(t, self.disconnect)
        self.timer.start()
        self.logger.debug('timer set in set_timer')

    def create_db(self, name):
        create_db = "create database %s" % name
        self.cursor().execute(create_db)
        self.logger.debug('created database %s' % name)

    # ------------------------------ Common functions ------------------------------ #
    def show_all_databases(self):
        self.connect()
        self.logger.debug('show_all_databases was called')
        show_databases = "show databases"
        cursor = self.cursor()
        try:
            cursor.execute(show_databases)
            self.logger.debug('returned all databases')
            return cursor.fetchall()
        except Exception as e:
            self.logger.error('Failed to show databases %s' % e)

    def show_all_tables(self):
        self.connect()
        self.logger.debug('show_all_tables was called')
        show_tables = "show tables"
        cursor = self.cursor()
        try:
            cursor.execute(show_tables)
            self.logger.debug('returned all tables')
            return cursor.fetchall()
        except Exception as e:
            self.logger.error('Failed to show tables %s' % e)

    def create_bot_users_data_table(self):
        self.connect()
        self.logger.debug('create bot users data table was called')
        create_bot_users_data = """
        create table bot_users_data(
            chat_id int not null primary key,
            username varchar(32),
            group_chat_id int references bot_groups(group_chat_id),
            first_name varchar(64),
            last_name varchar(64)
        )"""
        cursor = self.cursor()
        try:
            cursor.execute(create_bot_users_data)
            self.logger.info('Created bot_users_data_table')
        except Exception as e:
            self.logger.error('failed to create bot users data table %s' % e)

    def create_bot_users_scores_table(self):
        self.connect()
        create_bot_users_scores = """
        create table bot_users_scores(
            chat_id int not null primary key references bot_users_data(chat_id),
            score int,
            nosm int,
            nofm int,
            norm int,
            nosw int,
            nosv int,
            nosa int,
            nosp int
        )"""
        cursor = self.cursor()
        try:
            cursor.execute(create_bot_users_scores)
            self.logger.info('Created bot_users_scores_table')
        except Exception as e:
            self.logger.error('failed to create bot users scores table %s' % e)

    def create_bot_groups_table(self):
        self.connect()
        create_bot_groups = """
        create table bot_groups(
            group_name varchar(32),
            group_owner varchar(32),
            group_chat_id int,

            primary key(group_chat_id)
        )
        """
        cursor = self.cursor()
        try:
            cursor.execute(create_bot_groups)
            self.logger.info('Created bot_groups_table')
        except Exception as e:
            self.logger.error('failed to create bot groups table %s' % e)

    def add_user(self, chat_id, username, group_chat_id, first_name, last_name):
        self.connect()
        self.logger.debug('new user %s is about to be added to database' % username)
        insert_user = "insert into bot_users_data (chat_id, username, group_chat_id, first_name, last_name) values (%s, %s, %s, %s, %s)"
        val = (chat_id, username, group_chat_id, first_name, last_name)
        cursor = self.cursor()
        try:
            cursor.execute(insert_user, val)
            self.logger.info('Added user %s to database' % username)
        except Exception as e:
            self.logger.error('failed to add user %s' % e)

    def check_username(self, username):
        self.logger.debug('used check username')
        self.connect()
        select = "select * from bot_users_data where username = '%s'" % username
        cursor = self.cursor()
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got username')
            return result
        except Exception as e:
            self.logger.info("User is not in database! : %s" % e)
            return 0

    def check_chat_id(self, chat_id):
        self.logger.debug('used check chat_id')
        self.connect()
        select = "select * from bot_users_data where chat_id = '%s'" % chat_id
        cursor = self.cursor()
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got chat_id')
            return result
        except Exception as e:
            self.logger.info("Chat_id %s is not in database! : %s" % (chat_id, e))
            return 0

    def add_score(self, chat_id, score):
        self.logger.debug('used add score')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            s = result[1]
            s += score
            update = "update bot_users_scores set score = '%s' where chat_id = '%s'" % (s, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s score to %s" % (score, chat_id))
        except Exception as e:
            self.logger.error("Failed to add score! : %s" % e)
            self.mysql.rollback()

    def nosm_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosm inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosm = result[2]
            nosm += n
            update = "update bot_users_scores set nosm = '%s' where chat_id = '%s'" % (nosm, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s messages to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosm! : %s" % e)
            self.mysql.rollback()

    def nofm_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nofm inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nofm = result[3]
            nofm += n
            update = "update bot_users_scores set nofm = '%s' where chat_id = '%s'" % (nofm, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s forward to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nofm! : %s" % e)
            self.mysql.rollback()

    def norm_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used norm inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            norm = result[4]
            norm += n
            update = "update bot_users_scores set norm = '%s' where chat_id = '%s'" % (norm, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s reply to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase norm! : %s" % e)
            self.mysql.rollback()

    def nosw_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosw inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosw = result[5]
            nosw += n
            update = "update bot_users_scores set nosw = '%s' where chat_id = '%s'" % (nosw, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s words to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosw! : %s" % e)
            self.mysql.rollback()

    def nosv_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosv inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosv = result[6]
            nosv += n
            update = "update bot_users_scores set nosv = '%s' where chat_id = '%s'" % (nosv, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s voice to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosv! : %s" % e)
            self.mysql.rollback()

    def nosa_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosa inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosa = result[7]
            nosa += n
            update = "update bot_users_scores set nosa = '%s' where chat_id = '%s'" % (nosa, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s activitie to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosa! : %s" % e)
            self.mysql.rollback()

    def nosp_inc(self, chat_id, n):  # number of sent messages increment
        self.logger.debug('used nosp inc')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosp = result[8]
            nosp += n
            update = "update bot_users_scores set nosp = '%s' where chat_id = '%s'" % (nosp, chat_id)
            cursor.execute(update)
            self.mysql.commit()
            self.logger.info("Added %s project to %s" % (n, chat_id))
        except Exception as e:
            self.logger.error("Failed to increase nosp! : %s" % e)
            self.mysql.rollback()

    def get_user(self, chat_id=None, username=None):
        self.logger.debug('used get user')
        self.connect()
        cursor = self.cursor()
        if chat_id:
            try:
                select = "select * from bot_users_data where chat_id = '%s'" % chat_id
                cursor.execute(select)
                result = cursor.fetchone()
                self.logger.debug('got user')
                return result
            except Exception as e:
                self.logger.error("Failed to get user information %s %s" % (chat_id, e))
        elif username:
            try:
                get_chat_id = "select * from bot_users_data where username = '%s'" % username
                cursor.execute(get_chat_id)
                result = cursor.fetchone()
                chat_id = result[0]
                try:
                    select = "select * from bot_users_data where chat_id = '%s'" % chat_id
                    cursor.execute(select)
                    result = cursor.fetchone()
                    self.logger.debug('got user')
                    return result
                except Exception as e:
                    self.logger.error("Failed to get user information %s : %s" % (chat_id, e))
            except Exception as e:
                self.logger.error("Failed to get chat id! : %s" % e)

    def get_chat_id(self, username):
        self.logger.debug('used get chat_id')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_data where username = '%s'" % username
        try:
            cursor.execute(select)
            user = cursor.fetchone()
            chat_id = user[0]
            self.logger.debug("got chat_id")
            return chat_id
        except Exception as e:
            self.logger.error("Failed to get chat_id : %s" % e)

    def calculate_rank(self, chat_id):
        self.logger.debug('used calculate rank')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_users_scores order by score desc"  # should I add ` ?
        u = self.get_user(chat_id)  # to get user
        user_group = u[2]  # to get user's group
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            rank = 0
            for result in results:
                tmp_chat_id = result[0]
                user = self.get_user(tmp_chat_id)
                group = user[2]
                if group == user_group:
                    rank += 1
                    if result[0] == chat_id:
                        return rank
        except Exception as e:
            self.logger.error("Failed to calculate %s rank : %s" % (chat_id, e))
            return 0  # should take care when using this function that if returned 0 means failed

    def get_score(self, chat_id):
        self.logger.debug('used get score')
        self.connect()
        cursor = self.cursor()
        try:
            select = "select * from bot_users_scores where chat_id = '%s'" % chat_id
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got score')
            return result
        except Exception as e:
            self.logger.error("Failed to get user information %s : %s" % (chat_id, e))

    def is_owner(self, chat_id):
        self.logger.debug('used is_owner')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_admins where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            if result['level'] == 'owner':  # should check if the user is owner for example result[7]
                self.logger.debug("got owner")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error("Failed to check owner : %s" % e)
            return -1  # means error

    def is_group_owner(self, chat_id, group_chat_id):
        self.logger.debug('used is_group_owner')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_admins where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            if result['level'] == 'owner':  # should check if the user is owner for example result[7]
                self.logger.debug("got owner")
                if result['group_chat_id'] == group_chat_id:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            self.logger.error("Failed to check admin : %s" % e)
            return -1  # means error

    def is_assistant(self, chat_id):
        self.logger.debug('used is_assistant')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_admins where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            if result['level'] == 'assistant':  # should check if the user is owner for example result[7]
                self.logger.debug("got assistant")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error("Failed to check assistant : %s" % e)
            return -1  # means error

    def is_group_assistant(self, chat_id, group_chat_id):
        self.logger.debug('used is_group_assistant')
        self.connect()
        cursor = self.cursor()
        select = "select * from bot_admins where chat_id = '%s'" % chat_id
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            if result['level'] == 'assistant':  # should check if the user is owner for example result[7]
                self.logger.debug("got assistant")
                if result['group_chat_id'] == group_chat_id:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            self.logger.error("Failed to check assistant : %s" % e)
            return -1  # means error

    def check_group_chat_id(self, chat_id):
        self.logger.debug('used chaeck_group_chat_id')
        self.connect()
        select = "select * from bot_groups where chat_id = '%s'" % chat_id
        cursor = self.cursor()
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            self.logger.debug('got group_chat_id')
            return result
        except Exception as e:
            self.logger.info('group_chat_id %s is not in database : %s' % (chat_id, e))
            return 0

# ------------------------------ MongoDB ------------------------------ #

# Maybe MongoDB later

# ------------------------------ other databases ------------------------------ #

# Send to server / External DataBase with API

# ------------------------------ Objects ------------------------------ #

sqlite = SqliteDB()
mysql = MysqlDB()
