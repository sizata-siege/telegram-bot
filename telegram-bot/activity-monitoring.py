# IN THE NAME OF GOD
# Activity monitoring bot v7.0
# add admin menu
# add /post = /job
# save user chatid in database
# Save group chatid in database
# set limit for scores by admin for example if less than 400 per week then warn both admin and the user
# release score board in group for admin
# /mtn = /maintenance (maintenance)
# add notebook option and create a file for each users notes
# add contact admin and save the message and then send for admin or send the data in a database and admin see them in his panel inbox when he wants
# add contact manager = admin
# add suggestion option
# add report a problem option
# add a check list that users write their plan for the future and then they check(mark) their activities and also admin and manager can see their activities
# ALTER TABLE `test` ADD `123` INT NOT NULL AFTER `str`;
# custom select users stats full . avg length of messages
# add challenge adding to admin panel
# context.bot.sendMessage(username = 'IR_SIZATA_SIEGE', text='Hi')
# setting.json <<< auto score activities = 0 ,auto score projects
# /maintenance >>> for i in groups send planned a maintenance for 30 mins
# add a groups list and add the chai id s to it
# parse mode and html design in messages
# job_queue = updater.job_queue
# ravanshenasi user based on somethings like average message length
# add some schedule for admin panel to set the auto-reset period ( monthly / weekly / ... )
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-JobQueue

version = 7.0
# -------------------------Import tools------------------------- #
from time import sleep
from datetime import datetime
import json
# -------------------------Import Telegram------------------------- #
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction, ParseMode

# Token = "656547710:AAFciOC_C4Ch1KJDjRu0CTKc_UJT1aR3tms"
Token = "1017559271:AAG-Rj4fc14ondDY9ABeVfzdK2PkFEMvmhs"
updater = Updater(token=Token, use_context=True)
dp = updater.dispatcher
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# -------------------------Connect to DataBase------------------------- #
import sqlite3

con = sqlite3.connect("bot.db", check_same_thread=False)
admins = ["IR_SIZATA_SIEGE", "alireza_rhm99"]


# -------------------------Functions------------------------- #
def time():
    now = str(datetime.now())
    return now[0:10] + '-' + now[11:13] + '-' + now[14:16] + '-' + now[17:19]


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
            score = result[5] + 30
            score += words
            update_m = "update bot_users set nosm = %s where username = '%s'" % (nosm, user)
            update_w = "update bot_users set nosw = %s where username = '%s'" % (nosw, user)
            update_s = "update bot_users set score = %s where username = '%s'" % (score, user)
            cursor.execute(update_m)
            cursor.execute(update_w)
            cursor.execute(update_s)
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
            score = result[5] + 35
            score += words
            update_s = "update bot_users set score = %s where username = '%s'" % (score, user)
            cursor.execute(update_s)
            update_f = "update bot_users set nofm = %s where username = '%s'" % (nofm, user)
            update_w = "update bot_users set nosw = %s where username = '%s'" % (nosw, user)
            cursor.execute(update_f)
            cursor.execute(update_w)
            con.commit()
            print("Forwarded > %s > %s words" % (user, words))
        except:
            print("Error updating!")
            con.rollback()


def scoreReply(user, text, isGroup):
    if isGroup:
        cursor = con.cursor()
        select = "select * from bot_users where username = '%s'" % user
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            norm = result[4] + 1
            words = text.count(" ") + 1
            nosw = result[3] + words
            update_r = "update bot_users set norm = %s where username = '%s'" % (norm, user)
            update_w = "update bot_users set nosw = %s where username = '%s'" % (nosw, user)
            cursor.execute(update_r)
            cursor.execute(update_w)
            score = result[5] + 40
            score += words
            update_s = "update bot_users set score = %s where username = '%s'" % (score, user)
            cursor.execute(update_s)
            con.commit()
            print("Replied > %s > %s words" % (user, words))
        except:
            print("Error updating!")
            con.rollback()


def addUser(user):
    if user:
        cursor = con.cursor()
        add = "insert into bot_users VALUES ('%s', 0, 0, 0, 0, 0, 0, 0)" % user
        try:
            cursor.execute(add)
            con.commit()
            print("added %s to database!" % user)
        except:
            print("Error add!")
            con.rollback()
    else:
        # context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⚠️U don't have username.⚠️\npls set a username first" % name)
        # Unavalable because of context
        print("Not added. Invalid username!")


def Start(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    name = update.message.from_user.first_name
    # context.bot.sendMessage(user_id='SIZATA_Se7en', text='Hi')
    if int(chatid) < 0:
        if update.effective_chat.id == 753039129 or update.effective_chat.id == 106652269:
            context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
            sleep(3)
            context.bot.sendMessage(chat_id=update.effective_chat.id, text="✅ Bot started ✅")
            context.bot.sendMessage(chat_id=update.effective_chat.id,
                                    text="⚠️All messages will affect users activity⚠️")
            print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", user,
                  " >>> start in group")
        else:
            context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
            sleep(3)
            context.bot.sendMessage(chat_id=update.effective_chat.id, text="🚫You can't start the bot in group🚫")
    else:
        btns = [
            [InlineKeyboardButton("📉 میزان فعالیت من 📈", callback_data="Mystats")],
            [InlineKeyboardButton("امتیاز دیگر کاربران", callback_data="scores")],
            [InlineKeyboardButton("📊 روش محاسبه فعالیت 📊", callback_data="MeasurMethod")],
            [InlineKeyboardButton("👑رتبه من👑", callback_data="Myrank"),
             InlineKeyboardButton("🆕ورژن ربات🆕", callback_data="Version")],
            [InlineKeyboardButton("فرستادن پروژه / کارکرد", callback_data="Send")]
            # [InlineKeyboardButton("Test Option 1", callback_data = "test"),
            # InlineKeyboardButton("Test Option 2", callback_data = "test")]
        ]
        start_markup = InlineKeyboardMarkup(btns)
        context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text="Hi %s! 👋\nHow can I help U?" % name,
                                reply_markup=start_markup)
        print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ",
              update.message.from_user.username, " >>> start in PV")


def Text(update, context):
    # print("Text called")
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
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text="✅ User %s added to Controled users ✅" % username)
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
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text="✅ User %s added to Controled users ✅" % username)
        scoreForwarded(username, text, isGroup)


def Stats(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    text = update.message.text
    if int(update.effective_chat.id) < 0:
        isGroup = 1
        print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ",
              update.message.from_user.username, " >>> stats in group")
    elif update.effective_chat.id == 753039129 or update.effective_chat.id == 106652269:  # user in admins
        isGroup = 0
        print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ",
              update.message.from_user.username, " >>> stats in PV")
        cursor = con.cursor()
        select = "select * from bot_users ORDER BY `score` DESC"
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            for result in results:
                user = result[0]
                nosm = result[1]
                nofm = result[2]
                nosw = result[3]
                norm = result[4]
                score = result[5]
                nosa = result[6]
                nosp = result[7]
                context.bot.sendMessage(chat_id=update.effective_chat.id,
                                        text="%s ➡️ (%s) Score 🔸 (%s) M 🔸 (%s) F 🔸 (%s) R 🔸 (%s) W 🔸 (%s) A 🔸 (%s) P" % (
                                            user, score, nosm, nofm, norm, nosw, nosa, nosp))
        except:
            print("Error printing in stats!")
    else:
        print("Unable!")


def MyRank(update, context):
    query = update.callback_query
    user = query.from_user.username
    chatid = query.message.chat_id
    print("%s >>> Myrank" % user)
    cursor = con.cursor()
    # select = "select * from bot_users ORDER BY 'score' DESC"#Wrong '    `
    select = "select * from bot_users ORDER BY `score` DESC"
    try:
        cursor.execute(select)
        results = cursor.fetchall()
        i = 0
        for result in results:
            i += 1
            if result[0] == user:
                context.bot.sendMessage(chat_id=chatid, text="شما رتبه %s هستید!" % i)
    except:
        print("Error printing rank!")


def Mystats(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if int(update.effective_chat.id) < 0:
        isGroup = 1
        print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ",
              update.message.from_user.username, " >>> MyStats in group")
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="🚫You can't use this command in the group🚫")
    else:
        query = update.callback_query
        isGroup = 0
        print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ",
              update.message.from_user.username, " >>> MyStats in PV")
        cursor = con.cursor()
        select = "select * from bot_users where username = '%s'" % user
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            user = result[0]
            nosm = result[1]
            nofm = result[2]
            norm = result[4]
            score = result[5]
            nosa = result[6]
            nosp = result[7]
            context.bot.sendMessage(chat_id=update.effective_chat.id,
                                    text="%s➡️(%s) Score🔸(%s) Messages🔸(%s) Forwards🔸(%s) Replies🔸(%s) Activity🔸(%s) Projects" % (
                                        user, score, nosm, nofm, norm))
        except:
            print("Error printing!")
            context.bot.sendMessage(chat_id=update.effective_chat.id, text="❌Failed to send your data❌")


def mystats(update, context):
    query = update.callback_query
    user = query.from_user.username
    chatid = query.message.chat_id
    # user = update.message.from_user.username
    if int(chatid) < 0:
        print(chatid, " ", user, " ", " >>> MyStats in group")
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=chatid, text="🚫You can't use this command in the group🚫")
    else:
        print(chatid, " ", user, " ", " >>> MyStats in PV")
        cursor = con.cursor()
        select = "select * from bot_users where username = '%s'" % user
        try:
            cursor.execute(select)
            result = cursor.fetchone()
            user = result[0]
            nosm = result[1]
            nofm = result[2]
            norm = result[4]
            score = result[5]
            nosa = result[6]
            nosp = result[7]
            context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            sleep(3)
            context.bot.sendMessage(chat_id=chatid,
                                    text="%s➡️(%s) Score🔸(%s) Messages🔸(%s) Forwards🔸(%s) Replies🔸(%s) Activity🔸(%s) Projects" % (
                                        user, score, nosm, nofm, norm, nosa, nosp))
        except:
            print("Error printing!")
            context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            sleep(3)
            context.bot.sendMessage(chat_id=chatid, text="❌Failed to send your data❌")


def Reply(update, context):
    if int(update.effective_chat.id) < 0:
        isGroup = 1
    else:
        isGroup = 0
    username = update.message.from_user.username
    text = update.message.text
    if checkUsername(username):
        scoreReply(username, text, isGroup)
    else:
        addUser(username)
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text="✅ User %s added to Controled users ✅" % username)
        scoreReply(username, text, isGroup)


def Create(update, context):
    create = """create table bot_users(
        username TEXT(100),
        nosm INTEGER,
        nofm INTEGER,
        nosw INTEGER,
        norm INTEGER,
        score INTEGER,
        nosa INTEGER,
        nosp INTEGER)"""
    cursor = con.cursor()
    cursor.execute(create)
    con.commit()
    print("Created Table!!!")
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="Created table!!!")


def CreateAdmins(update, context):
    create = """create table bot_admins(
        username TEXT(100),
        chatid TEXT(20))"""
    cursor = con.cursor()
    cursor.execute(create)
    con.commit()
    print("Created Admins Table!!!")
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="Created table!!!")


def NewAdmin(update, context):
    admin = update.message.text[11:]
    print(admin)


def Status(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(1)
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="✅ Bot is Online! ✅")
    print(update.effective_chat.id, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name,
          " ", update.message.from_user.username, " >>> Status")


def ResetAll(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if user in admins:
        # context.bot.deleteMessage(chat_id = update.effective_chat.id, message_id = update.message.message_id)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="⏳Checking scores!⏳")
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="🌐Updating database!🌐")
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="✅Reseted all scores!✅")
        cursor = con.cursor()
        select = "select * from bot_users"
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            for result in results:
                nosm = 0
                nofm = 0
                nosw = 0
                norm = 0
                score = 0
                nosa = 0
                nosp = 0
                update_m = "update bot_users set nosm = %s" % nosm
                update_f = "update bot_users set nofm = %s" % nofm
                update_w = "update bot_users set nosw = %s" % nosw
                update_r = "update bot_users set norm = %s" % norm
                update_s = "update bot_users set score = %s" % score
                update_a = "update bot_users set nosa = %s" % nosa
                update_p = "update bot_users set nosp = %s" % nosp
                cursor.execute(update_m)
                cursor.execute(update_f)
                cursor.execute(update_w)
                cursor.execute(update_r)
                cursor.execute(update_s)
                cursor.execute(update_a)
                cursor.execute(update_p)
                con.commit()
            print("Reset All")
            context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            sleep(3)
            context.bot.sendMessage(chat_id=update.effective_chat.id, text="⚠️All data was reset by admin!⚠️")
        except:
            print("Error updating!")
            con.rollback()
    else:
        print("%s tried to reset data!" % user)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="❌U R not admin!❌")


def CheckScores(update, context):
    user = update.message.from_user.username
    chatid = update.message.chat_id
    print("%s >>> Check scores" % user)
    if user == "IR_SIZATA_SIEGE":
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="⏳Checking scores!⏳")
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="🌐Updating database!🌐")
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="✅Scores Updated!✅")
        cursor = con.cursor()
        select = "select * from bot_users"
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            for result in results:
                username = result[0]
                nosm = result[1]
                nofm = result[2]
                nosw = result[3]
                norm = result[4]
                score = result[5]
                rescore = nosm * 30 + nofm * 35 + nosw + norm * 40
                if score == rescore:
                    print("Scores checked successfully! No diffrence found!")
                else:
                    print("%s >>> Score doesn't match! Updating Score!" % user)
                    update_s = "update bot_users set score = %s where username = '%s'" % (rescore, username)
                    cursor.execute(update_s)
                    con.commit()
        except:
            print("failed to check scores")
            con.rollback()
    else:
        print("%s >>> check scores" % user)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text="❌U R not admin!❌")


def Op(update, context):
    key = [
        [InlineKeyboardButton("option1", callback_data="100"),
         InlineKeyboardButton("option1", callback_data="200")],
        [InlineKeyboardButton("option1", callback_data="300"),
         InlineKeyboardButton("option1", callback_data="400")],
        [InlineKeyboardButton("option1", callback_data="500")],
        [InlineKeyboardButton("option1", callback_data="600")],
        [InlineKeyboardButton("option1", callback_data="700")]
    ]
    printkey = InlineKeyboardMarkup(key)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(3)
    context.bot.sendMessage(chat_id=update.effective_chat.id,
                            text="Hi! 👋\nHow can I help U?\n/mystats >>> فعالیت من در تبادل اطلاعات",
                            reply_markup=printkey)


def test(update, context):
    query = update.callback_query
    user = query.from_user.username
    chatid = query.message.chat_id
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(3)
    context.bot.sendMessage(chat_id=chatid, text="😊 This is a test option, so it doesn't work! 😁")
    print(user, ">>> test option")


def MeasurMethod(chatid, context):
    context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
    sleep(5)
    context.bot.sendMessage(chat_id=chatid,
                            text="Messages X 30\nForwards X 35\nReplies X 40\nWords X 1\nبرای مثال پیامی که طولش 4 کلمه هست امتیاز 34 میگیره و پیامی که 9 کلمه هست 39 امتیاز داره . اکه ریپلای باشه به همین صورت!")


def Version(chatid, context):
    context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
    sleep(3)
    context.bot.sendMessage(chat_id=chatid, text="@activity_monitoring_bot  version %s" % version)


def Echo(update, context):
    user = update.message.from_user.username
    chatid = update.effective_chat.id
    text = update.message.text[5:]
    if user in admins:
        context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=text)
        print("Echo by %s >>> %s" % (update.message.from_user.username, text))
    else:
        context.bot.deleteMessage(chat_id=chatid, message_id=update.message.message_id)
        print("Failed to echo %s by %s" % (text, user))


def Del(update, context):
    user = update.message.from_user.username
    chatid = update.effective_chat.id
    n = int(update.message.text[5:])
    i = 0
    if user in admins:
        print("Deleted %s messages by %s" % (n, user))
        while i <= n:
            try:
                context.bot.deleteMessage(chat_id=update.effective_chat.id, message_id=update.message.message_id - i)
                i += 1
            except:
                print("Missing message")
                i += 1
                n += 1
    else:
        context.bot.deleteMessage(chat_id=chatid, message_id=update.message.message_id)
        print("%s failed to delete %s messages(Access Denied)" % (user, n))


def DelUser(update, context):
    target = update.message.text[10:]
    user = update.message.from_user.username
    if user in admins:
        cursor = con.cursor()
        remove = "DELETE FROM `bot_users` WHERE `username`='%s'" % target
        try:
            cursor.execute(remove)
            print("removed %s" % target)
            context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            sleep(3)
            update.message.reply_text("⚠️Successfully removed %s" % target)
            con.commit()
        except:
            context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            sleep(3)
            update.message.reply_text("❌Failed to remove %s" % target)
            print("failed to remove %s" % target)
            con.rollback()
    else:
        print("%s failed to remove %s" % (user, target))
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(3)
        update.message.reply_text("❌Access Denied❌")


def AddScore(update, context):
    user = update.message.from_user.username
    text = update.message.text[11:]
    print(text)
    if user in admins:
        target = text.split(',')[0]
        score = text.split(',')[1]

    # /add_score target,3000


def Scores(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if int(update.effective_chat.id) > 0:
        print(chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ",
              update.message.from_user.username, " >>> scores in PV")
        cursor = con.cursor()
        select = "select * from bot_users ORDER BY `score` DESC"
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            for result in results:
                user = result[0]
                # nosm = result[1]
                # nofm = result[2]
                # nosw = result[3]
                # norm = result[4]
                score = result[5]
                context.bot.sendMessage(chat_id=update.effective_chat.id, text="%s ➡️ (%s) Score" % (user, score))
        except:
            print("Error printing in stats!")


def Scores_options(update, context, user):
    chatid = update.effective_chat.id
    if int(update.effective_chat.id) > 0:
        print(chatid, " ", user, " >>> scores in PV")
        cursor = con.cursor()
        select = "select * from bot_users ORDER BY `score` DESC"
        try:
            cursor.execute(select)
            results = cursor.fetchall()
            for result in results:
                user = result[0]
                # nosm = result[1]
                # nofm = result[2]
                # nosw = result[3]
                # norm = result[4]
                score = result[5]
                context.bot.sendMessage(chat_id=update.effective_chat.id, text="%s ➡️ (%s) Score" % (user, score))
        except:
            print("Error printing in stats!")


def Send(update, context):
    reply_keyboard = [['/send_activity\nکارکرد', '/send_project\nپروژه']]
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(3)
    context.bot.sendMessage(chat_id=update.effective_chat.id,
        text='لطفا یک دسته بندی انتخاب کنید.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


def CQH(update, context):
    query = update.callback_query
    chatid = query.message.chat_id
    user = query.message.from_user.username
    if query.data == "Mystats":
        mystats(update, context)
    elif query.data == "test":
        test(update, context)
    elif query.data == "MeasurMethod":
        MeasurMethod(chatid, context)
    elif query.data == "Myrank":
        MyRank(update, context)
    elif query.data == "Version":
        Version(chatid, context)
    elif query.data == "scores":
        Scores_options(update, context, user)
    elif query.data == "Send":
        Send(update, context)
    #ADMIN PANEL
    elif query.data == 'showActivities':
        ShowActivities(query, context)
    elif query.data == 'showProjects':
        ShowProjects(query, context)
    elif query.data == 'addChallenge':
        AddChallenge(update, context)
    elif query.data == 'addScore':
        pass
        #AddScore_option(update, context)
    elif query.data == 'asa':
        AutoScoreActivities(update, context)
    elif query.data == 'asp':
        AutoScoreProjects(update, context)
    elif query.data == 'vacation':
        Vacation(update, context)


def ShowActivities(update, context):
    print(update.message.from_user.username, '>>> showActivities')
    f = open('activity_file.txt', 'r')
    for line in f.readlines():
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(2)
        try:
            date = line.split(',')[0]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing date❌')
            break
        try:
            user = line.split(',')[1]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing User❌')
            break
        try:
            category = line.split(',')[2]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing Category❌')
            break
        try:
            subject = line.split(',')[3]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing Subject❌')
            break
        try:
            description = line.split(',')[4]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing Description❌')
            break
        try:
            if category == 'Website':
                context.bot.sendMessage(chat_id=update.message.chat_id, text='📅' + date + '\n\n👤' + user + '\n\n🌐' + category + '🌐\n\n🔶' + subject + '\n\n🔷' + description)
            elif category == 'Android':
                context.bot.sendMessage(chat_id=update.message.chat_id, text='📅' + date + '\n\n👤' + user + '\n\n📱' + category + '📱\n\n🔶' + subject + '\n\n🔷' + description)
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌failed to list❌')
            break
    context.bot.sendMessage(chat_id=update.message.chat_id, text='🔶🔶FINISH🔶🔶')
        #📅, 👤, 🔶, 🔷, 🌐, 📱


def ShowProjects(update, context):
    print(update.message.from_user.username, '>>> showProjects')
    f = open('project_file.txt', 'r')
    for line in f.readlines():
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(2)
        try:
            date = line.split(',')[0]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing date❌')
            break
        try:
            user = line.split(',')[1]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing user❌')
            break
        try:
            category = line.split(',')[2]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing category❌')
            break
        try:
            subject = line.split(',')[3]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing subject❌')
            break
        try:
            description = line.split(',')[4]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing description❌')
            break
        try:
            picture_file = line.split(',')[5]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing pic❌')
            break
        try:
            video_file = line.split(',')[6]
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text='❌missing video❌')
            break
        if category == 'Website':
            context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open(picture_file, 'rb'), caption='📅' + date + '\n\n👤' + user + '\n\n🌐' + category + '🌐\n\n🔶' + subject + '\n\n🔷' + description)
        elif category == 'Android':
            context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open(picture_file, 'rb'), caption='📅' + date + '\n\n👤' + user + '\n\n🌐' + category + '🌐\n\n🔶' + subject + '\n\n🔷' + description)
        if video_file == 'no-video.mp4\n':
            context.bot.sendMessage(chat_id=update.message.chat_id, text='no video')
        else:
            context.bot.sendVideo(chat_id=update.message.chat_id, video=open(video_file[:-1], 'rb'))
    context.bot.sendMessage(chat_id=update.message.chat_id, text='🔶🔶FINISH🔶🔶')


def Admin(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if user in admins:
        print("%s loged in as admin" % user)
        btns = [
            [InlineKeyboardButton('📋 Activities 📋', callback_data='showActivities'),
            InlineKeyboardButton('📁 Projects 📁', callback_data='showProjects')],
            [InlineKeyboardButton('🏅 Add Challenge 🏅', callback_data='addChallenge')],
            [InlineKeyboardButton('☣️ Add Score to someone ☣️', callback_data='addScore')],
            [InlineKeyboardButton('😴 مرخصی 😴', callback_data='vacation')],
            [InlineKeyboardButton('Auto score activities : %s' % 'on', callback_data='asa')],
            [InlineKeyboardButton('Auto score projects : %s' % 'on', callback_data='asp')]
        ]
        admin_markup = InlineKeyboardMarkup(btns)
        #data_list = loadData()
        context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
        sleep(5)
        context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
        sleep(5)
        context.bot.sendMessage(chat_id=chatid, text="Welcome Sir !😎\n", reply_markup=admin_markup)# activities : 3 \n projects : 5
    else:
        print("%s is not admin" % user)
        context.bot.send_chat_action(chat_id=chatid, action=ChatAction.TYPING)
        sleep(3)
        context.bot.sendMessage(chat_id=chatid, text="U R not admin!")


def Post(update, context):
    user = update.message.from_user.username
    chatid = update.effective_chat.id
    if update.message.text[1] == 'p':
        text = update.message.text[6:]
    else:
        text = update.message.text[5:]
    context.bot.deleteMessage(chat_id=chatid, message_id=update.message.message_id)
    cursor = con.cursor()
    select = "select * from bot_users where username = '%s'" % user
    try:
        cursor.execute(select)
        result = cursor.fetchone()
        post = result[8]
        print("Successfully fetched post from database!")
    except:
        print("Failed to fetch user post from database!")
    content = """ <b>%s</b>
    <h1>(%s)</h1>


    %s

    """% (post, user, text)
    # post + '\n( ' + user + ' )\n' + '\n' + text
    context.bot.sendMessage(chat_id=chatid, text=content, parse_mode=ParseMode.HTML)


def Validate(file):
    try:
        myfile = open(file, 'r')
    except:
        myfile = open(file, 'w')
        myfile.close()


# -------------------------Conversations------------------------- #
user_activity = " "
CATEGORY_A, SUBJECT_A, DESCRIPTION_A = range(3)


def SendActivity(update, context):
    Validate('activity_file.txt')
    user = update.message.from_user.username
    print("%s  >>> SendActivity" % user)
    reply_keyboard = [['Website', 'Android']]  # 📱 🌐
    global user_activity
    user_activity = ''
    user_activity += "%s,%s," % (str(datetime.now()), user)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(1)
    update.message.reply_text(
        'شما میتوانید با استفاده از /cancel فرایند را در هر جایی پایان دهید. لطفا دسته بندی را انتخاب کنید!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return CATEGORY_A


def category_a(update, context):
    text = update.message.text
    global user_activity
    user_activity += "%s," % text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('بسیار خب. حالا موضوع کارکردتو بفرست. مثلا :\nیادگیری زبان جدید',
                              reply_markup=ReplyKeyboardRemove())
    return SUBJECT_A


def subject_a(update, context):
    text = update.message.text
    global user_activity
    user_activity += "%s," % text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('حالا توضیحات رو بفرست. مثلا: \nمن یادگیری زبان جاواسکریپت رو شروع کردم.')
    return DESCRIPTION_A


def description_a(update, context):
    text = update.message.text
    global user_activity
    user_activity += "%s\n" % text
    f = open('activity_file.txt', 'a')
    f.write(user_activity)
    f.close()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('کارکرد شما در انتظار تایید است و پس از تایید امتیاز به شما افزوده خواهد شد')
    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user.username
    update.message.reply_text('فرایند لغو شد!',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


#                    ==========                      #
user_project = " "
CATEGORY, SUBJECT, DESCRIPTION, PHOTO, VIDEO, FILE = range(6)


def SendProject(update, context):
    Validate('project_file.txt')
    user = update.message.from_user.username
    print("%s  >>> SendProject" % user)
    reply_keyboard = [['Website', 'Android']]
    global user_project
    user_project = ''
    user_project += "%s,%s," % (str(datetime.now()), user)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(1)
    update.message.reply_text(
        'شما میتوانید با استفاده از /cancel فرایند را در هر جایی پایان دهید. لطفا دسته بندی را انتخاب کنید!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return CATEGORY


def category(update, context):
    text = update.message.text
    global user_project
    user_project += "%s," % text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('بسیار خب. حالا موضوع کارکردتو بفرست. مثلا :\nیادگیری زبان جدید',
                              reply_markup=ReplyKeyboardRemove())
    return SUBJECT


def subject(update, context):
    text = update.message.text
    global user_project
    user_project += "%s," % text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('حالا توضیحات رو بفرست. مثلا: \nمن یادگیری زبان جاواسکریپت رو شروع کردم.')
    return DESCRIPTION


def description(update, context):
    text = update.message.text
    global user_project
    user_project += "%s," % text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('اگه از پروژت عکس داری برام بفرست اگر نه از /skip استفاده کن.')
    return PHOTO


def photo(update, context):
    user = update.message.from_user.username
    photo_file = update.message.photo[-1].get_file()
    t = time()
    photo_file.download('media/%s-%s.jpg' % (user, t))
    global user_project
    user_project += "media/%s-%s.jpg," % (user, t)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('اگه از پروژت فیلم داری برام بفرست اگرنه از /skip استفاده کن.')
    return VIDEO


def video(update, context):
    user = update.message.from_user.username
    # video_file = update.message.video[-1].get_file()
    video_id = update.message.video.file_id
    video_file = context.bot.get_file(video_id)
    t = time()
    video_file.download('media/%s-%s.mp4' % (user, t))
    global user_project
    user_project += "media/%s-%s.mp4\n" % (user, t)
    f = open('project_file.txt', 'a')
    f.write(user_project)
    f.close()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('پروژه شما ذخیره شد و پس از تایید امتیاز شما افزوده خواهد شد')
    # update.message.reply_text('گرفتمش حالا فایل پروژه رو برام بفرست یا از /skip استفاده کن.')
    # return FILE
    return ConversationHandler.END


def SkipPhoto(update, context):
    print("No photo recived")
    global user_project
    user_project += "no-photo.jpg,"
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('اگه از پروژت فیلم داری برام بفرست اگرنه از /skip استفاده کن.')
    return VIDEO


def SkipVideo(update, context):
    print("No video recived")
    global user_project
    user_project += "no-video.mp4\n"
    f = open('project_file.txt', 'a')
    f.write(user_project)
    f.close()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    update.message.reply_text('پروژه شما ذخیره شد و پس از تایید امتیاز شما افزوده خواهد شد')
    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user.username
    print("%s canceled the proccess!" % user)
    update.message.reply_text('فرایند لغو شد',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


# -------------------------Handlers------------------------- #
start_handler = CommandHandler('start', Start)
stats_handler = CommandHandler('stats', Stats)
mystats_handler = CommandHandler('mystats', Mystats)
option_handler = CommandHandler('op', Op)
create_handler = CommandHandler('create', Create)
create_admins_handler = CommandHandler('create_admins', CreateAdmins)
new_admin_handler = CommandHandler('new_admin', NewAdmin)
status_handler = CommandHandler('status', Status)
reset_all_handler = CommandHandler('reset_all', ResetAll)
check_scores_handler = CommandHandler('check_scores', CheckScores)
echo_handler = CommandHandler('echo', Echo)
del_handler = CommandHandler('del', Del)
del_user_handler = CommandHandler('del_user', DelUser)
add_score_handler = CommandHandler('add_score', AddScore)
admin_handler = CommandHandler('admin', Admin)
scores_handler = CommandHandler('scores', Scores)
post_handler = CommandHandler('post', Post)
job_handler = CommandHandler('job', Post)
# manager_handler = CommandHandler('XYZ', AddAdmin)
text_handler = MessageHandler(Filters.text, Text)
forwarded_handler = MessageHandler(Filters.forwarded, Forwarded)
reply_handler = MessageHandler(Filters.reply, Reply)
cqh_handler = CallbackQueryHandler(CQH)
# -------------------------Conversation Handlers------------------------- #
send_activity_handler = ConversationHandler(
    entry_points=[CommandHandler('send_activity', SendActivity)],

    states={
        CATEGORY_A: [MessageHandler(Filters.regex('^(Website|Android)$'), category_a)],

        SUBJECT_A: [MessageHandler(Filters.text, subject_a)],

        DESCRIPTION_A: [MessageHandler(Filters.text, description_a)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)
send_project_handler = ConversationHandler(
    entry_points=[CommandHandler('send_project', SendProject)],

    states={
        CATEGORY: [MessageHandler(Filters.regex('^(Website|Android)$'), category)],

        SUBJECT: [MessageHandler(Filters.text, subject)],

        DESCRIPTION: [MessageHandler(Filters.text, description)],

        PHOTO: [MessageHandler(Filters.photo, photo),
                CommandHandler('skip', SkipPhoto)],

        VIDEO: [MessageHandler(Filters.video, video),
                CommandHandler('skip', SkipVideo)]

        # FILE: [MessageHandler(Filters.document, file)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)
# -------------------------Add Handlers------------------------- #
dp.add_handler(send_activity_handler)
dp.add_handler(send_project_handler)
dp.add_handler(start_handler)
dp.add_handler(stats_handler)
dp.add_handler(mystats_handler)
dp.add_handler(create_handler)
dp.add_handler(create_admins_handler)
dp.add_handler(new_admin_handler)
dp.add_handler(status_handler)
dp.add_handler(reset_all_handler)
dp.add_handler(reply_handler)
dp.add_handler(forwarded_handler)
dp.add_handler(text_handler)
dp.add_handler(option_handler)
dp.add_handler(cqh_handler)
dp.add_handler(echo_handler)
dp.add_handler(del_handler)
dp.add_handler(del_user_handler)
dp.add_handler(check_scores_handler)
dp.add_handler(admin_handler)
dp.add_handler(scores_handler)
dp.add_handler(add_score_handler)
dp.add_handler(post_handler)
dp.add_handler(job_handler)
# -------------------------||||||||||||------------------------- #
updater.start_polling()
updater.idle()
# -------------------------||||||||||||------------------------- #
# CLI robots
# API robots
# what is CLI?

# import mysql.connector
# con = mysql.connector.connect(
#     user = "xoEe4hNkKr",
#     password = "dxFTpB2adi",
#     host = "remotemysql.com",
#     database = "xoEe4hNkKr"
#     # user = "sizata99",
#     # password = "sizata709152331402",
#     # host = "sizata99.mysql.pythonanywhere-services.com",
#     # database = "sizata99$bot"
# )
# /echo ربات به مدت 10 دقیقه غیرفعال میشود
