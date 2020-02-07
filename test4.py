#IN THE NAME OF GOD
#Activity monitoring bot v1

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
Token = "919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM"
updater = Updater(token = Token, use_context = True)
dp = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#-------------------------Connect to DataBase-------------------------#
import mysql.connector
con = mysql.connector.connect(
    user = "xoEe4hNkKr",
    password = "dxFTpB2adi",
    host = "remotemysql.com",
    database = "xoEe4hNkKr"
)
#-------------------------Functions-------------------------#
def checkUsername(user):
    cursor = con.cursor()
    select = "select * from bot_users where username = '%s'" % user
    try:
        cursor.execute(select)
        result = cursor.fetchone()
        return result
    except:
        print("Error selection !")
        return 0
def scoreText(user, text, isGroup):
    if isGroup:
        cursor = con.cursor()
        select = "select * from bot_users where username = '%s'" % user
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nosm = result[1] + 1
            words = text.count(" ") + 1
            nosw = result[3] + words
            update_m = "update bot_users set nosm = %s where username = '%s'" % (nosm, user)
            update_w = "update bot_users set nosw = %s where username = '%s'" % (nosw, user)
            cursor.execute(update_m)
            cursor.execute(update_w)
            con.commit()
            print("Text > %s > %s words" % (user, words))
        except:
            print("Error updating!")
            con.rollback()
def scoreForwarded(user, text, isGroup):
    if isGroup:
        cursor = con.cursor()
        select = "select * from bot_users where username = '%s'" % user
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            nofm = result[2] + 1
            words = text.count(" ") + 1
            nosw = result[3] + words
            update_f = "update bot_users set nofm = %s where username = '%s'" % (nofm, user)
            update_w = "update bot_users set nosw = %s where username = '%s'" % (nosw, user)
            cursor.execute(update_f)
            cursor.execute(update_w)
            con.commit()
            print("Forwarded > %s > %s words" % (user, words))
        except:
            print("Error updating!")
            con.rollback()
def addUser(user):
    cursor = con.cursor()
    add = "insert into bot_users VALUES ('%s', 0, 0, 0)" % user
    try:
        cursor.execute(add)
        con.commit()
        print("added %s to database!" % user)
    except:
        print("Error add!")
        con.rollback()
def userStats():
    cursor = con.cursor()
    select = "select * from bot_users"
    try:
        cursor.execute(select)
        results = cursor.fetchall()
        for result in results:
            user = result[0]
            nosm = result[1]
            nofm = result[2]
            nosw = result[3]
            report[result] = "%s > %s messages & %s Forwards & %s words total" % (user, nosm, nofm, nosw)
            print(report[result])
    except:
        print("Error printing!")
def Start(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    name = update.message.from_user.first_name
    if int(chatid) < 0:
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ Bot started ✅")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⚠️All messages will effect users activity⚠️")
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> start in group")
    else:
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "Hi %s! 👋\nHow can I help U?" % name)
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> start in PV")
def Text(update, context):
    if int(update.effective_chat.id) < 0:
        isGroup = 1
    else:
        isGroup = 0
    username = update.message.from_user.username
    text = update.message.text
    if checkUsername(username):
        scoreText(username, text, isGroup)
    else:
        addUser(username)
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ User %s added to Controled users ✅" % username)
        scoreText(username, text, isGroup)
def Forwarded(update, context):
    if int(update.effective_chat.id) < 0:
        isGroup = 1
    else:
        isGroup = 0
    username = update.message.from_user.username
    text = update.message.text
    if checkUsername(username):
        scoreForwarded(username, text, isGroup)
    else:
        addUser(username)
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ User %s added to Controled users ✅" % username)
        scoreForwarded(username, text, isGroup)
def Reply(update, context):
    print("reply")
def Stats(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    text = update.message.text
    if int(update.effective_chat.id) < 0:
        isGroup = 1
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> stats in group")
    elif update.effective_chat.id == 753039129:
        isGroup = 0
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> stats in PV")
        cursor = con.cursor()
        select = "select * from bot_users"
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            for result in results:
                user = result[0]
                nosm = result[1]
                nofm = result[2]
                nosw = result[3]
                context.bot.sendMessage(chat_id = update.effective_chat.id, text = "%s➡️(%s) messages🔸(%s) Forwards🔸(%s) words total" % (user, nosm, nofm, nosw))
        except:
            print("Error printing!")
    else:
        print("Unable!")
def Mystats(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    text = update.message.text
    if int(update.effective_chat.id) < 0:
        isGroup = 1
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> MyStats in group")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "🚫You can't use this command in the group🚫")
    else:
        isGroup = 0
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> MyStats in PV")
        cursor = con.cursor()
        select = "select * from bot_users"
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            user = result[0]
            nosm = result[1]
            nofm = result[2]
            nosw = result[3]
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "%s➡️(%s) messages🔸(%s) Forwards" % (user, nosm, nofm))
        except:
            print("Error printing!")
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "❌Failed to send your data❌")
#-------------------------Handlers-------------------------#
start_handler = CommandHandler('start', Start)
stats_handler = CommandHandler('stats', Stats)
mystats_handler = CommandHandler('mystats', Mystats)
#reset_all_handler = CommandHandler('reset_all', ResetAll)
#manager_handler = CommandHandler('XYZ', AddAdmin)
text_handler = MessageHandler(Filters.text, Text)
forwarded_handler = MessageHandler(Filters.forwarded, Forwarded)
reply_handler = MessageHandler(Filters.reply, Reply)
#-------------------------Add Handlers-------------------------#
dp.add_handler(start_handler)
dp.add_handler(stats_handler)
dp.add_handler(mystats_handler)
#dp.add_handler(reset_all_handler)
dp.add_handler(reply_handler)
dp.add_handler(forwarded_handler)
dp.add_handler(text_handler)
#-------------------------||||||||||||-------------------------#
updater.start_polling()
updater.idle()