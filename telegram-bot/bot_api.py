# IN THE NAME OF GOD


from time import sleep
from datetime import datetime
import json
import logging
from bot_classes import *
from functions import *
# ------------------------- Import Telegram ------------------------- #
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction, ParseMode, MessageEntity
# ------------------------- Configuration ------------------------- #
from config import *
updater = Updater(token=Token, use_context=True)
dp = updater.dispatcher
# log to file
logging.basicConfig(filename='debug.log', format='%(asctime)s - %(levelname)-8s- %(name)-20s : %(message)s', level=logging.DEBUG)
# log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(name)-20s : %(message)')
console.setFormatter(console_formatter)
logging.getLogger('').addHandler(console)


