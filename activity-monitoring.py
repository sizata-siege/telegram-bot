# IN THE NAME OF GOD
# Activity monitoring bot v6.0
# add admin menu
# add /post = /job 
# save user chatid in database
# Save group chatid in database
# set limit for scotes by admin
# releaze score board in group for admin
# /mtn = /maintenance (maintenance)
# add notebook option and create a file for each users notes
# add contact admin and save the message and then send for admin or send the data in a database and admin see them in his panel inbox when he wants
# add contact manager = admin 
# add suggestion option
# add report a problem option
# add a check list that users write their plan for the future and then they check(mark) their activities and also admin and manager can see their activities
# ALTER TABLE `test` ADD `123` INT NOT NULL AFTER `str`; 
# custom select users stats full . avg length of messages
version = 6.0
POINTt = 0
POINT = 1
#-------------------------Import tools-------------------------#
from time import sleep
#-------------------------Import Telegram-------------------------#
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
#Token = "656547710:AAFciOC_C4Ch1KJDjRu0CTKc_UJT1aR3tms"
Token = "1017559271:AAG-Rj4fc14ondDY9ABeVfzdK2PkFEMvmhs"
updater = Updater(token = Token, use_context = True)
dp = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#-------------------------Connect to DataBase-------------------------#
import sqlite3
con = sqlite3.connect("bot.db", check_same_thread=False)
admins = ["IR_SIZATA_SIEGE", "alireza_rhm99"]
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
        add = "insert into bot_users VALUES ('%s', 0, 0, 0, 0, 0)" % user
        try:
            cursor.execute(add)
            con.commit()
            print("added %s to database!" % user)
        except:
            print("Error add!")
            con.rollback()
    else:
        #context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⚠️U don't have username.⚠️\npls set a username first" % name)
        #Unavalable because of context
        print("Not added. Invalid username!")
def Start(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    name = update.message.from_user.first_name
    if int(chatid) < 0:
        if update.effective_chat.id == 753039129 or update.effective_chat.id == 106652269:
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ Bot started ✅")
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⚠️All messages will effect users activity⚠️")
            print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", user, " >>> start in group")
        else:
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "🚫You can't start the bot in group🚫")
    else:
        btns = [
            [InlineKeyboardButton("📉 میزان فعالیت من 📈", callback_data = "Mystats")],
            [InlineKeyboardButton("📊 روش محاسبه فعالیت 📊", callback_data = "MeasurMethod")],
            [InlineKeyboardButton("👑رتبه من👑", callback_data = "Myrank"),
            InlineKeyboardButton("🆕ورژن ربات🆕", callback_data = "Version")],
            # [InlineKeyboardButton("Test Option 1", callback_data = "test"),
            # InlineKeyboardButton("Test Option 2", callback_data = "test")]
            [InlineKeyboardButton("امتیاز دیگر کاربران", callback_data = "scores")]
        ]
        start_markup = InlineKeyboardMarkup(btns)
        context.bot.sendMessage(chat_id = update.effective_chat.id, 
        text = "Hi %s! 👋\nHow can I help U?" % name, 
        reply_markup = start_markup)
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> start in PV")
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
def Stats(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    text = update.message.text
    if int(update.effective_chat.id) < 0:
        isGroup = 1
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> stats in group")
    elif update.effective_chat.id == 753039129 or update.effective_chat.id == 106652269:#user in admins
        isGroup = 0
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> stats in PV")
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
                context.bot.sendMessage(chat_id = update.effective_chat.id, text = "%s ➡️ (%s) Score 🔸 (%s) M 🔸 (%s) F 🔸 (%s) R 🔸 (%s) W" % (user, score, nosm, nofm, norm, nosw))
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
    #select = "select * from bot_users ORDER BY 'score' DESC"#Wrong '    `  
    select = "select * from bot_users ORDER BY `score` DESC"
    try:
        cursor.execute(select)
        results = cursor.fetchall()
        i = 0
        for result in results:
            i += 1
            if result[0] == user:
                context.bot.sendMessage(chat_id = chatid, text = "شما رتبه %s هستید!" % i)
    except:
        print("Error printing rank!")
def Mystats(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if int(update.effective_chat.id) < 0:
        isGroup = 1
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> MyStats in group")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "🚫You can't use this command in the group🚫")
    else:
        query = update.callback_query
        isGroup = 0
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> MyStats in PV")
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
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "%s➡️(%s) Score🔸(%s) Messages🔸(%s) Forwards🔸(%s) Replies" % (user, score, nosm, nofm, norm))
        except:
            print("Error printing!")
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "❌Failed to send your data❌")
def mystats(update, context):
    query = update.callback_query
    user = query.from_user.username
    chatid = query.message.chat_id
    #user = update.message.from_user.username
    if int(chatid) < 0:
        print (chatid, " ", user, " ", " >>> MyStats in group")
        context.bot.sendMessage(chat_id = chatid, text = "🚫You can't use this command in the group🚫")
    else:
        query = update.callback_query
        print (chatid, " ", user, " ", " >>> MyStats in PV")
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
            context.bot.sendMessage(chat_id = chatid, text = "%s➡️(%s) Score🔸(%s) Messages🔸(%s) Forwards🔸(%s) Replies" % (user, score, nosm, nofm, norm))
        except:
            print("Error printing!")
            context.bot.sendMessage(chat_id = chatid, text = "❌Failed to send your data❌")
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
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ User %s added to Controled users ✅" % username)
        scoreReply(username, text, isGroup)
def Create(update, context):
    create = """create table bot_users(
        username TEXT(100),
        nosm INTEGER,
        nofm INTEGER,
        nosw INTEGER,
        norm INTEGER,
        score INTEGER)"""
    cursor = con.cursor()
    cursor.execute(create)
    con.commit()
    print("Created Table!!!")
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "Created table!!!")
def CreateAdmins(update, context):
    create = """create table bot_admins(
        username TEXT(100),
        chatid TEXT(20))"""
    cursor = con.cursor()
    cursor.execute(create)
    con.commit()
    print("Created Admins Table!!!")
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "Created table!!!")
def NewAdmin(update, context):
    admin = update.message.text[11: ]
    print(admin)
def Status(update, context):
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅ Bot is Online! ✅")
    print (update.effective_chat.id, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> Status")
def ResetAll(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if user in admins:
        #context.bot.deleteMessage(chat_id = update.effective_chat.id, message_id = update.message.message_id)
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⏳Checking scores!⏳")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "🌐Updating database!🌐")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅Reseted all scores!✅")
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
                update_m = "update bot_users set nosm = %s" % nosm
                update_f = "update bot_users set nofm = %s" % nofm
                update_w = "update bot_users set nosw = %s" % nosw
                update_r = "update bot_users set norm = %s" % norm
                update_s = "update bot_users set score = %s" % score
                cursor.execute(update_m)
                cursor.execute(update_f)
                cursor.execute(update_w)
                cursor.execute(update_r)
                cursor.execute(update_s)
                con.commit()
            print("Reset All")
            context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⚠️All data was reset by admin!⚠️")
        except:
            print("Error updating!")
            con.rollback()
    else:
        print("%s tried to reset data!" % user)
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "❌U R not admin!❌")
def CheckScores(update, context):
    user = update.message.from_user.username
    chatid = update.message.chat_id
    print("%s >>> Check scores" % user)
    if user == "IR_SIZATA_SIEGE":
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "⏳Checking scores!⏳")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "🌐Updating database!🌐")
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "✅Scores Updated!✅")
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
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = "❌U R not admin!❌")
def Op(update, context):
    key = [
        [InlineKeyboardButton("option1", callback_data = "100"),
        InlineKeyboardButton("option1", callback_data = "200")],
        [InlineKeyboardButton("option1", callback_data = "300"),
        InlineKeyboardButton("option1", callback_data = "400")],
        [InlineKeyboardButton("option1", callback_data = "500")],
        [InlineKeyboardButton("option1", callback_data = "600")],
        [InlineKeyboardButton("option1", callback_data = "700")]
    ]
    printkey = InlineKeyboardMarkup(key)
    context.bot.sendMessage(chat_id = update.effective_chat.id, 
        text = "Hi! 👋\nHow can I help U?\n/mystats >>> فعالیت من در تبادل اطلاعات", 
        reply_markup = printkey)
def test(update, context):
    query = update.callback_query
    user = query.from_user.username
    chatid = query.message.chat_id
    context.bot.sendMessage(chat_id = chatid, text = "😊 This is a test option, so it doesn't work! 😁")
    print(user, ">>> test option")
def MeasurMethod(chatid, context):
    context.bot.sendMessage(chat_id = chatid, 
    text = "Messages X 30\nForwards X 35\nReplies X 40\nWords X 1\nبرای مثال پیامی که طولش 4 کلمه هست امتیاز 34 میگیره و پیامی که 9 کلمه هست 39 امتیاز داره . اکه ریپلای باشه به همین صورت!")
def Version(chatid, context):
    context.bot.sendMessage(chat_id = chatid, text = "@activity_monitoring_bot  version %s" % version)
def Echo(update, context):
    user = update.message.from_user.username
    chatid = update.effective_chat.id
    text = update.message.text[5: ]
    if user in admins:
        context.bot.deleteMessage(chat_id = update.effective_chat.id, message_id = update.message.message_id)
        context.bot.sendMessage(chat_id = update.effective_chat.id, text = text)
        print("Echo by %s >>> %s" % (update.message.from_user.username, text))
    else:
        context.bot.deleteMessage(chat_id = chatid, message_id = update.message.message_id)
        print("Failed to echo %s by %s" % (text, user))
def Del(update, context):
    user = update.message.from_user.username
    chatid = update.effective_chat.id
    n = int(update.message.text[5: ])
    i = 0
    if user in admins:
        print("Deleted %s messages by %s" % (n, user))
        while i <= n:
            try:
                context.bot.deleteMessage(chat_id = update.effective_chat.id, message_id = update.message.message_id - i)
                i += 1
            except:
                print("Missing message")
                i += 1
                n += 1
    else:
        context.bot.deleteMessage(chat_id = chatid, message_id = update.message.message_id)
        print("%s failed to delete %s messages(Access Denied)" % (user, n))
def DelUser(update, context):
    target = update.message.text[10: ]
    user = update.message.from_user.username
    if user in admins:
        cursor = con.cursor()
        remove = "DELETE FROM `bot_users` WHERE `username`='%s'" % target
        try:
            cursor.execute(remove)
            print("removed %s" % target)
            update.message.reply_text("⚠️Successfully removed %s" % target)
            con.commit()
        except:
            update.message.reply_text("❌Failed to remove %s" % target)
            print("failed to remove %s" % target)
            con.rollback()
    else:
        print("%s failed to remove %s" %(user, target))
        update.message.reply_text("❌Access Denied❌" )
def AddScore(update, context):
    user = update.message.from_user.username
    text = update.message.text[11: ]
    print(text)
    if user in admins:
        target = text.split(',')[0]
        score = text.split(',')[1]

    #/add_score target,3000
def Scores(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if int(update.effective_chat.id) > 0:
        print (chatid, " ", update.message.from_user.first_name, " ", update.message.from_user.last_name, " ", update.message.from_user.username, " >>> scores in PV")
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
                context.bot.sendMessage(chat_id = update.effective_chat.id, text = "%s ➡️ (%s) Score" % (user, score))
        except:
            print("Error printing in stats!")
def Scores_options(update, context, user):
    chatid = update.effective_chat.id
    if int(update.effective_chat.id) > 0:
        print (chatid, " ", user, " >>> scores in PV")
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
                context.bot.sendMessage(chat_id = update.effective_chat.id, text = "%s ➡️ (%s) Score" % (user, score))
        except:
            print("Error printing in stats!")
def Rep(update, context):
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
def Admin(update, context):
    chatid = update.effective_chat.id
    user = update.message.from_user.username
    if user in admins:
        print("%s is admin" % user)
        context.bot.sendMessage(chat_id = chatid, text = "U R admin!")
    else:
        print("%s is not admin" % user)
        context.bot.sendMessage(chat_id = chatid, text = "U R not admin!")
#--------------------------------------------------------------------
def SendActivity(update, context):
    #reply_keyboard = [['a', 'b', 'c']]
    update.message.reply_text('Hi !!!')#, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    print("POINT1")
    return POINTt
def ttt(update, context):
    update.message.reply_text('I see! Please send me a photo of yourself')#, reply_markup=ReplyKeyboardRemove())
    print("POINT2")
    return POINT
def skip_ttt(update, context):
    print("skipped")
def sss(update, context):
    update.message.reply_text('FUCK U !!!')
    return ConversationHandler.END
def cancel(update, context):
    print("canceled!!!")
#-------------------------Handlers-------------------------#
start_handler = CommandHandler('start', Start)
stats_handler = CommandHandler('stats', Stats)
mystats_handler = CommandHandler('mystats', Mystats)
option_handler = CommandHandler('op', Op)
rep_handler = CallbackQueryHandler(Rep)
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
#manager_handler = CommandHandler('XYZ', AddAdmin)
text_handler = MessageHandler(Filters.text, Text)
forwarded_handler = MessageHandler(Filters.forwarded, Forwarded)
reply_handler = MessageHandler(Filters.reply, Reply)
#-------------------------Conversation Handlers-------------------------#
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('send_activity', SendActivity)],
    states={
        POINTt : [MessageHandler(Filters.text, ttt), CommandHandler('skip', skip_ttt)],

        POINT : [MessageHandler(Filters.text, sss), CommandHandler('skip', skip_ttt)]

        #    ,LOCATION: [MessageHandler(Filters.location, location),
        #               CommandHandler('skip', skip_location)],

        #    BIO: [MessageHandler(Filters.text, bio)]
    },

    fallbacks = [CommandHandler('cancel', cancel)]

)
#-------------------------Add Handlers-------------------------#
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
dp.add_handler(rep_handler)
dp.add_handler(echo_handler)
dp.add_handler(del_handler)
dp.add_handler(del_user_handler)
dp.add_handler(check_scores_handler)
dp.add_handler(admin_handler)
dp.add_handler(scores_handler)
dp.add_handler(add_score_handler)
dp.add_handler(conv_handler)
#-------------------------||||||||||||-------------------------#
updater.start_polling()
updater.idle()
#-------------------------||||||||||||-------------------------#
#CLI robots
#API robots
#what is CLI?

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
#/echo ربات به مدت 10 دقیقه غیرفعال میشود