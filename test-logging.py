import logging

logging.basicConfig(filename='test-logging.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(filename='test-logging.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
logging.basicConfig(filename='test-logging.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

logging.log(msg='Hi all', level=logging.ERROR)
logging.log(msg='Hi all', level=logging.INFO)
logging.log(msg='Hi all', level=logging.WARNING)


