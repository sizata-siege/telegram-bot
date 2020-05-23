from bot_classes import *
from scoring_rules import *
from database import *
from time import sleep
#
# Amir = User(74318907438, "@amir", ['tabadol'], "amirhosseyn", "shakery", "TD")
#
# print(Amir)

import logging
logging.basicConfig(filename='logs/test.log', format='%(asctime)s %(levelname)-8s: %(name)-20s-%(message)s', level=logging.DEBUG)
# logging.debug("this is a test detail")
# logging.info("this is an info")
# logging.warning("this is a warning")
# a = 10
# logging.debug("Hi all %s" % a)
# logging.info("Hi all %s" % a)
# logging.warning("Hi all %s" % a)
# logging.error("Hi all %s" % a)

# formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(name)-20s : %(message)')
# file1 = logging.FileHandler('test1.log')
# file1.setFormatter(formatter)
# logger1 = logging.getLogger('logger1')
# logger1.setLevel(logging.INFO)
# logger1.addHandler(file1)
#
# file2 = logging.FileHandler('test2.log')
# file2.setFormatter(formatter)
# logger2 = logging.getLogger('logger2')
# logger2.setLevel(logging.DEBUG)
# logger2.addHandler(file2)
#
# logger1.info('an info')
# logger2.info('an info')
#
# logger1.debug('debug')
# logger2.debug('debug')

# db1 = MysqlDB()
# db1.connect()
# db1.create_bot_users_data_table()
# logging.info('finish')
# db1.disconnect()


