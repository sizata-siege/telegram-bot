#IN THE NAME OF GOD 
#SIEGE ASSISTANT version 7.0 || uses file to save scores and usernames
#write all logs on cloud or server
import pyttsx3
from os import system
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from time import sleep
Token = "919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM"
updater = Updater(token = Token, use_context = True)
dp = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

id = 0
chat_id_var = ""
logger = "-1001309221311"
#logger = "753039129"
#-------------------------Connect to DataBase-------------------------#
import pymysql
find_chatid = "select * from bot_users where chatid = "
find_test = "select * from bot_users where name = 'test'"
#-------------------------Speech-------------------------#
def Say(p):
	#e = engine
	e = pyttsx3.init()
	e.setProperty('rate' , 175)
	voices = e.getProperty('voices')
	e.setProperty('voice' , voices[1].id)
	e.setProperty('volume',1.0)
	e.say(p)
	e.runAndWait()
Say("Engine Started")
#-------------------------Functions-------------------------#
def Start(update, context):
	Say("user started the bot")
	chatid = update.effective_chat.id
	# connector = pymysql.connect('remotemysql.com','zZg4TSbkYB','r9F4W0h329','zZg4TSbkYB')
	# cursor = connector.cursor()
	# chack database
	context.bot.send_message(chat_id = update.effective_chat.id , text = "Hi {} {} 😐. WTF R U going to do ?\n/help".format(update.message.from_user.first_name , update.message.from_user.last_name))
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
	context.bot.send_message(chat_id = "119940830" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> start")

def Reg_help(update, contexe):
    	context.bot.send_message(chat_id = update.effective_chat.id, text = "لطفا به صورت زیر ثبت نام کنید : \n/register fullname")

def Register(update, context):
	fullname = update.message.text[10: ]
	username = update.message.from_user.username
	tfname = update.message.from_user.first_name
	tlname = update.message.from_user.last_name
	post = "NOT SET YET"
	chatid = update.effective_chat.id
	adb = "NOT ADDED YET"
	score = 0
	nofm = 0
	nosa = 0
	nosm = 0
	nosn = 0
	norm = 0

	connector = pymysql.connect('remotemysql.com','zZg4TSbkYB','r9F4W0h329','zZg4TSbkYB')
	cursor = connector.cursor()
	cursor.execute("insert into bot_users values({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(id, fullname, fullname, username, tfname, tlname, post, chatid, adb, score, nofm, nosa, nosm, nosn, norm))
	#cursor.execute(f"insert into bot_users values({id}, {fullname}, {fullname}, {username}, {tfname}, {tlname}, {post}, {chatid}, {adb}, {score}, {nofm}, {nosa}, {nosm}, {nosn}, {norm})")
	connector.commit()

	#connector.rollback()
	#print("ERROR")
    #fname = "test"# How to get from user????

def Chatid(update, context):
	Say("chat-id request detected, sending chat-id")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "Sorry! Unable to send your chat_id now.😔")
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ chat_id".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> chat_id")

def Help(update, context):
	Say("client requested help, sending help content")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "/version ➡️ Version\n\n/admin ➡️ Admin panel\n\n/chat_id ➡️ Show chat_id\n\n/myjob ➡️ Your job\n\n/send_activity ➡️ Send activity\n\n/send_project ➡️ Send project\n\n/notice ➡️ Send a new message (Notice) in the group as your name\n\n/google ➡️ Search in google\n\n/ping ➡️ Check the connection of bot\n\n/latency ➡️ The same as ping")
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ help".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> help")

def Version(update, context):
	Say("version request recived, sending version information")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "SIEGE ASSISTANT version 7.0")
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ version".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> version")

def Admin(update, context):
	Say("client claimed admin")
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️❓admin❓".format(update.message.from_user.first_name , update.message.from_user.last_name))
	context.bot.send_message(chat_id = update.effective_chat.id , text = "⌛️ Prepairing ⌛️")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  admin ?")
	sleep(2)
	context.bot.send_message(chat_id = update.effective_chat.id , text = "🆔 Checking ID 🆔")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking ID ")
	Say("checking ID")
	sleep(3)
	context.bot.send_message(chat_id = update.effective_chat.id , text = "⌛️ Checking Username ⌛️")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking Username ")
	Say("checking username")
	sleep(2)
	context.bot.send_message(chat_id = update.effective_chat.id , text = "⌛️ Checking Info ⌛️")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking Information ")
	sleep(3)
	context.bot.send_message(chat_id = update.effective_chat.id , text = "🌐 Connecting to server 🌐")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Connecting to server ")
	sleep(4)
	context.bot.send_message(chat_id = update.effective_chat.id , text = "🌐 Connecting to database 🌐")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Connecting to database ")
	sleep(5)
	if update.effective_chat.id == 119940830: #(or update.message.from_user.username == "@SIZATA_SIEGE")
		context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ✅ Admin detected ✅".format(update.message.from_user.first_name , update.message.from_user.last_name))
		context.bot.send_message(chat_id = update.effective_chat.id , text = "✅ Admin detected ✅")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Admin detected ")
		Say("admin detected")
		sleep(2)
		context.bot.send_message(chat_id = update.effective_chat.id , text = "⌛️ Prepairing your panel ⌛️")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Preparing panel ")
		Say("preparing panel")
		sleep(2)
		context.bot.send_message(chat_id = update.effective_chat.id , text = "❌ ERROR ❌")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  X  ERROR  X ")
		Say("error")
	else:
		context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ❌ Not admin ❌".format(update.message.from_user.first_name , update.message.from_user.last_name))
		context.bot.send_message(chat_id = update.effective_chat.id , text = "❌ U R Not admin ! 😐 ❌")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  X  Not admin  X ")
		Say("user is not admin")

def Myjob(update, context):
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ my job".format(update.message.from_user.first_name , update.message.from_user.last_name))
	Say("user needs to know his job, sending content")
	#job = "Send a request to database or server =/ and fetch data" #(username : ... | command : job | Yourjob is ... means u should ...
	context.bot.send_message(chat_id = update.effective_chat.id , text = "job")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> my-job")

def Send_activity(update, context):
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ send_activity_method".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  send_activity")
	Say("send-activity request recived, preparing to get it")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "Ok. Now send me your activity !")
	#wait to get data and send them to server or database | server should zip it and save it
	Say("got it, saving")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "Got it. \n⌛️ Saving ... ⌛️")
	sleep(3)
	Say("saving Successful")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "✅ Successful ✅")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> Successful")

def Notice(update, context):#need stickers
	context.bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ notice".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  notice")
	Say("notice command detected, prepairing")
	context.bot.send_message(chat_id = update.effective_chat.id , text = "Alright. What are you going to releaze ???")
	text = "The sent message"
	releazeText = "[{JOB}] {realname} \n\n {text} \n\n {#}{JOB}"#.format(from database by requesting job and nickname)
	context.bot.send_message(chat_id = update.effective_chat.id , text = "That's the preview. Are U sure U want to send it ???")
	#if yes :
	#	context.bot.send_message(chat_id = group_chat_id , text = releazeText)
	#	Say("releazed successfully")
	#	else cancel
	#	send the log to the server as success or fail and save the files and increase the sent messages for example
#-------------------------Handlers-------------------------#
start_handler = CommandHandler('start', Start)
help_handler = CommandHandler('help', Help)
version_handler = CommandHandler('version', Version)
admin_handler = CommandHandler('admin', Admin)
chatid_handler = CommandHandler('chat_id', Chatid)
myjob_handler = CommandHandler('myjob', Myjob)
send_activity_handler = CommandHandler('send_activity', Send_activity)
notice_handler = CommandHandler('notice', Notice)
register_handler = CommandHandler('register', Register)
reg_help_handler = CommandHandler('reg_help', Reg_help)
#-------------------------Add Handlers-------------------------#
dp.add_handler(start_handler)				#1
dp.add_handler(help_handler)				#2
dp.add_handler(version_handler)				#3
dp.add_handler(admin_handler)				#4
dp.add_handler(chatid_handler)				#5
dp.add_handler(myjob_handler)				#6
dp.add_handler(send_activity_handler)		#7
dp.add_handler(notice_handler)				#8
dp.add_handler(register_handler)
dp.add_handler(reg_help_handler)
#-------------------------||||||||||||-------------------------#
updater.start_polling()
updater.idle()
#-------------------------Old functions-------------------------#
# def start_method(bot , update):
#     	Say("user started the bot, checking ip, ip detected, sending result")
# 	bot.send_message(chat_id = update.message.chat_id , text = "Hi {} {} 😐. WTF R U going to do ?\n/help".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	bot.send_message(chat_id = "119940830" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> start")

# def chat_id_method(bot , update):
# 	Say("chat-id request detected, sending chat-id")
# 	bot.send_message(chat_id = update.message.chat_id , text = "Sorry! Unable to send your chat_id now.😔")
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ chat_id".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> chat_id")

# def help_method(bot , update):
# 	Say("client requested help, sending help content")
# 	bot.send_message(chat_id = update.message.chat_id , text = "/version ➡️ Version\n\n/admin ➡️ Admin panel\n\n/chat_id ➡️ Show chat_id\n\n/myjob ➡️ Your job\n\n/send_activity ➡️ Send activity\n\n/send_project ➡️ Send project\n\n/notice ➡️ Send a new message (Notice) in the group as your name\n\n/google ➡️ Search in google\n\n/ping ➡️ Check the connection of bot\n\n/latency ➡️ The same as ping")
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ help".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> help")

# def bot_version_method(bot , update):
# 	Say("version request recived, sending version information")
# 	bot.send_message(chat_id = update.message.chat_id , text = "SIEGE ASSISTANT version 6.0")
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ version".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> version")

# def admin_method(bot , update):
# 	Say("client claimed admin")
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️❓admin❓".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Prepairing ⌛️")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  admin ?")
# 	sleep(2)
# 	bot.send_message(chat_id = update.message.chat_id , text = "🆔 Checking ID 🆔")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking ID ")
# 	Say("checking ID")
# 	sleep(3)
# 	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Checking Username ⌛️")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking Username ")
# 	Say("checking username")
# 	sleep(2)
# 	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Checking Info ⌛️")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking Information ")
# 	sleep(3)
# 	bot.send_message(chat_id = update.message.chat_id , text = "🌐 Connecting to server 🌐")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Connecting to server ")
# 	sleep(4)
# 	bot.send_message(chat_id = update.message.chat_id , text = "🌐 Connecting to database 🌐")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Connecting to database ")
# 	sleep(5)
# 	if update.message.chat_id == 119940830: #(or update.message.from_user.username == "@SIZATA_SIEGE")
# 		bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ✅ Admin detected ✅".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 		bot.send_message(chat_id = update.message.chat_id , text = "✅ Admin detected ✅")
# 		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Admin detected ")
# 		Say("admin detected")
# 		sleep(2)
# 		bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Prepairing your panel ⌛️")
# 		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Preparing panel ")
# 		Say("preparing panel")
# 		sleep(2)
# 		bot.send_message(chat_id = update.message.chat_id , text = "❌ ERROR ❌")
# 		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  X  ERROR  X ")
# 		Say("error")
# 	else:
# 		bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ❌ Not admin ❌".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 		bot.send_message(chat_id = update.message.chat_id , text = "❌ U R Not admin ! 😐 ❌")
# 		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  X  Not admin  X ")
# 		Say("user is not admin")

# def my_job_method(bot , update):
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ my job".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	Say("user needs to know his job, sending content")
# 	#job = "Send a request to database or server =/ and fetch data" #(username : ... | command : job | Yourjob is ... means u should ...
# 	bot.send_message(chat_id = update.message.chat_id , text = "job")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> my-job")

# def send_activity_method(bot , update):#should be used as both
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ send_activity_method".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  send_activity")
# 	Say("send-activity request recived, preparing to get it")
# 	bot.send_message(chat_id = update.message.chat_id , text = "Ok. Now send me your activity !")
# 	#wait to get data and send them to server or database | server should zip it and save it
# 	Say("got it, saving")
# 	bot.send_message(chat_id = update.message.chat_id , text = "Got it. \n⌛️ Saving ... ⌛️")
# 	sleep(3)
# 	Say("saving Successful")
# 	bot.send_message(chat_id = update.message.chat_id , text = "✅ Successful ✅")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> Successful")

# def send_project_method(bot , update):#shouldn't be used , old
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ send_project_method".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  send_project")
# 	bot.send_message(chat_id = update.message.chat_id , text = "Ok. Now send me your project !")
# 	#wait to get data and send them to server or database | server should zip it and save it
# 	bot.send_message(chat_id = update.message.chat_id , text = "Got it. \n⌛️ Saving ... ⌛️")
# 	sleep(3)
# 	bot.send_message(chat_id = update.message.chat_id , text = "✅ Successful ✅")
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> Successful")

# def notice_method(bot , update):#need stickers
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ notice".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  notice")
# 	Say("notice command detected, prepairing")
# 	bot.send_message(chat_id = update.message.chat_id , text = "Alright. What are you going to releaze ???")
# 	text = "The sent message"
# 	releazeText = "[{JOB}] {realname} \n\n {text} \n\n {#}{JOB}"#.format(from database by requesting job and nickname)
# 	bot.send_message(chat_id = update.message.chat_id , text = "That's the preview. Are U sure U want to send it ???")
# 	#if yes :
# 	#	bot.send_message(chat_id = group_chat_id , text = releazeText)
# 	#	Say("releazed successfully")
# 	#	else cancel
# 	#	send the log to the server as success or fail and save the files and increase the sent messages for example

# def ping_method(bot , update):
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ Ping check ...".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking ping ... ")
# 	Say("ping request recived, pinging 4 2 2 4 with 32 bytes of data")
# 	system("ping 4.2.2.4")
# 	ping = "ping of google"
# 	#ping = system("pint 4.2.2.4")
# 	bot.send_message(chat_id = update.message.chat_id , text = ping)# how to measure ping in python (the function or the liberrary)

# def photo_detecter_test (bot , update):
# 	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ sent a picture".format(update.message.from_user.first_name , update.message.from_user.last_name))
# 	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  sent a picture")
# 	bot.send_message(chat_id = update.message.chat_id , text = "U have sent me a photo")

# def gb_method (bot , update):
# 	keyboard = [

# 				[InlineKeyboardButton("option 1" , callback_data="1"),
# 				InlineKeyboardButton("option 2" , callback_data="2")],
# 				[InlineKeyboardButton("option 3" , callback_data="3")]



# 				]
# 	reply_markup = InlineKeyboardMurkup(keyboard)
# 	update.message.reply_text("pls choose !" , reply_markup = reply_markup)

# def custom_keyboard (bot , update):
# 	custom_keyboard = [['top-left', 'top-right'], 
#                    	   ['bottom-left', 'bottom-right']]
# 	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
# 	bot.send_message(chat_id=chat_id, 
#                  text="Custom Keyboard Test", 
#                  reply_markup=reply_markup)

# def text_AI (bot , update):
# 	#bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
# 	text = update.message.text
# 	print(text)
# 	if "hi" in update.message.text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
# 	elif "Hi" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
# 	elif "hello" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "Hello 👋")
# 	elif "Hello" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "Hello 👋")
# 	elif "slm" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "slm 👋")
# 	elif "salam" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "salam 👋")
# 	elif "سلام" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "سلام 👋")
# 	elif "sghl" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "سلام")

# 	if "الو" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "جانم ؟")

# 	if "خوبی" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "سپاسگزارم. شما چطور هستید ؟")
# 	elif "چطوری" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "عالی. سپاسگزارم. شما چطور هستید ؟")

# 	if "عالی" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
# 	elif "عالیم" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
# 	elif "خوب" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
# 	elif "خوبم" in text:
# 		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
# 	#elif "" in text:
# 	#	bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")	
#-------------------------Old handlers-------------------------#
# #all commands should be closed in group except some interesting and special methods and commands =/
# updater.dispatcher.add_handler(CommandHandler('start' , start_method))-
# updater.dispatcher.add_handler(CommandHandler('help' , help_method))-
# updater.dispatcher.add_handler(CommandHandler('version' , bot_version_method))-
# updater.dispatcher.add_handler(CommandHandler('admin' , admin_method))-
# updater.dispatcher.add_handler(CommandHandler('chat_id' , chat_id_method))-
# updater.dispatcher.add_handler(CommandHandler('myjob' , my_job_method))-
# updater.dispatcher.add_handler(CommandHandler('send_activity' , send_activity_method))-
# updater.dispatcher.add_handler(CommandHandler('send_project' , send_project_method))
# updater.dispatcher.add_handler(CommandHandler('notice' , notice_method))-#for sending an important message in the group as a formal notification or message | for exaple : masoul fani : U have problem or the check starts at 8:00
# #updater.dispatcher.add_handler(CommandHandler('google' , google_method))#should search a phrase in google and show the resault
# updater.dispatcher.add_handler(CommandHandler('ping' , ping_method))#It shouldn't be a key =\
# updater.dispatcher.add_handler(CommandHandler('latency' , ping_method))#It shouldn't be a key =\
# updater.dispatcher.add_handler(CommandHandler('gbgbgb' , gb_method))
# #updater.dispatcher.add_handler(MessageHandler('k' , custom_keyboard))
# #updater.dispatcher.add_handler(MessageHandler(Filters.photo , photo_detecter_test))
# updater.dispatcher.add_handler(MessageHandler(Filters.text , text_AI))

#custom keyboards
#func (start , start)


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


#google search history


#----------DATABASE----------#
#all logs
#number of all sent data and messagess
#google search history


#----------FUTURE DATABASE----------#
#add an event
#add a challenge
#add a purpose
#add some hadis or find the hadises from the internet


#----------ACTIVITY MEASURING----------#
#sent messages x1 (anti spam should be applied)
#sent notifications or posts x5
#replayed messages x10
#number of messages which contains name of other members x1 fo each name
#number of replies that relates to sent message x10


#----------PACKET STRUCTURE----------#
#Filename = ASCII(Sender or member) + date(based on second) + subject + encryption_method(UIAXETCQ, b, c, ...)
#password