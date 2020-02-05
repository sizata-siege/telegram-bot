#IN THE NAME OF GOD
#Activity monitoring bot v1

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
Token = "656547710:AAFciOC_C4Ch1KJDjRu0CTKc_UJT1aR3tms"
updater = Updater(token = Token, use_context = True)
dp = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#-------------------------Connect to DataBase-------------------------#
import sqlite3
db = sqlite3.connect("bot.db")
cursor = db.cursor()
create_tb = """create table users(
    username TEXT(100) PRIMARY key,
    nosm INTEGER,
    nofm INTEGER)"""

#-------------------------Functions-------------------------#
def checkUsername(user):
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    select = "select * from users where %s = username" % user
    print(select)
    try:
        cursor.execute(select)
        result = cursor.fetchone()
        print(result)
        return result
    except:
        print("Error selection !")
        #cursor.execute(create_tb)
        print("Created table !")
        return 0
def scoreText(user, text):
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    select = "select * from users where username = %s" % user
    try:
        cursor.execute(select)
        result = cursor.fetchone()
        nosm = result[1] + 1
        update = "update users set nosm = %s where username = %s" % (nosm, user)
        cursor.execute(update)
        db.commit()
        print("Updated!")
    except:
        print("Error updating!")
        db.rollback()
def addUser(user):
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    add = "insert into users VALUES (%s, 0, 0)" % user
    try:
        cursor.execute(add)
        db.commit()
        print("added!")
    except:
        print("Error add!")
        db.rollback()
def Start(update, context):
    chatid = update.effective_chat.id
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ Bot started ✅")
    print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> start")
def Text(update, context):
    username = update.message.from_user.username
    text = update.message.text
    if checkUsername(username):
        scoreText(username, text)
    else:
        addUser(username)
        scoreText(username, text)
    print(username, " : ", text)
def Forwarded(update, context):
    text = update.message.text
    print(text)
def Stats(update, context):
    print(" >>> Stats")
#-------------------------Handlers-------------------------#
start_handler = CommandHandler('start', Start)
stats_handler = CommandHandler('stats', Stats)
text_handler = MessageHandler(Filters.text, Text)
forwarded_handler = MessageHandler(Filters.forwarded, Forwarded)
#-------------------------Add Handlers-------------------------#
dp.add_handler(start_handler)
dp.add_handler(stats_handler)
dp.add_handler(text_handler)
dp.add_handler(forwarded_handler)
#-------------------------||||||||||||-------------------------#
updater.start_polling()
updater.idle()