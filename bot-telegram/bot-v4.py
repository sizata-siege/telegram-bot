#IN THE NAME OF GOD 
#SIEGE ASSISTANT version 4.0
#write all logs on cloud or server
#use functions for less length
#solve the problem of glass buttom

from os import system
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackQueryHandler
#from telegram import InlineKeyboardButton , InlineKeyboardMurkup , ReplyKeyboardMarkup
from time import sleep

updater = Updater("919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM")

#def func (message , func):
#	updater.dispatcher.add_handler(CommandHandler('message' , func))
chat_id_var = ""
logger = "-1001309221311"
#logger = "753039129"
bot_progress_v = "وضعیت پیشرفت ربات"

def conLog(text):
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>> ", text)

def sendUser(text):
 	bot.send_message(chat_id = update.send_message.chat_id , text = text)

# def adminLog(text):
# 	bot.send_message(update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " ➡️ ", text)

def start_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "Hi {} {} 😐. WTF R U going to do ?\n/help".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.chat_id , update.message.from_user.first_name , update.message.from_user.last_name , update.message.from_user.username)#add name later
	#chat_id_var = "User "+update.message.chat_id+"started the bot"#add name in the future
	#bot.send_message(chat_id = "119940830" , text = "{} {} >>> start\n{}\n{}\n{}".format(update.message.from_user.first_name , update.message.from_user.last_name , update.message.chat_id , update.message.from_user.username))
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
	bot.send_message(chat_id = "119940830" , text = "{} {} ➡️ start".format(update.message.from_user.first_name , update.message.from_user.last_name))
	conLog("start")
	
	#send to channel

def chat_id_method(bot , update):
	bot.send_message(chat_id = update.send_message.chat_id , text = update.send_message.chat_id)
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ chat_id".format(update.message.from_user.first_name , update.message.from_user.last_name))
	conLog("chat_id")

def help_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "/bot_progress ➡️ "+bot_progress_v+"\n")
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ help".format(update.message.from_user.first_name , update.message.from_user.last_name))
	conLog("help")

def bot_version_method(bot , update):
	bot.send_message(chat_id = update.message.chat_id , text = "SIEGE ASSISTANT version 4.0")
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ version".format(update.message.from_user.first_name , update.message.from_user.last_name))
	conLog("version")

def admin_method(bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️❓admin❓".format(update.message.from_user.first_name , update.message.from_user.last_name))
	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Prepairing ⌛️")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  admin ?")
	sleep(2)
	bot.send_message(chat_id = update.message.chat_id , text = "🆔 Checking ID 🆔")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking ID ")
	sleep(3)
	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Checking Username ⌛️")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking Username ")
	sleep(2)
	bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Checking Info ⌛️")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking Information ")
	sleep(3)
	bot.send_message(chat_id = update.message.chat_id , text = "🌐 Connecting to server 🌐")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Connecting to server ")
	sleep(4)
	bot.send_message(chat_id = update.message.chat_id , text = "🌐 Connecting to database 🌐")
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Connecting to database ")
	sleep(5)
	if update.message.chat_id == 119940830: #(or update.message.from_user.username == "@SIZATA_SIEGE")
		bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ✅ Admin detected ✅".format(update.message.from_user.first_name , update.message.from_user.last_name))
		bot.send_message(chat_id = update.message.chat_id , text = "✅ Admin detected ✅")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Admin detected ")
		sleep(2)
		bot.send_message(chat_id = update.message.chat_id , text = "⌛️ Prepairing your panel ⌛️")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Preparing panel ")
		sleep(2)
		bot.send_message(chat_id = update.message.chat_id , text = "❌ ERROR ❌")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  X  ERROR  X ")
	else:
		bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ ❌ Not admin ❌".format(update.message.from_user.first_name , update.message.from_user.last_name))
		bot.send_message(chat_id = update.message.chat_id , text = "❌ U R Not admin ! 😐 ❌")
		print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  X  Not admin  X ")

def my_job_method(bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ my job".format(update.message.from_user.first_name , update.message.from_user.last_name))
	job = "Send a request to database or server =/ and fetch data" #(username : ... | command : job | Yourjob is ... means u should ...
	bot.send_massage(chat_id = update.message.chat_id , text = job)
	conLog("my_job")

def send_activity_method(bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ send_activity_method".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  send_activity")
	bot.send_message(chat_id = update.message.chat_id , text = "Ok. Now send me your activity !")
	#wait to get data and send them to server or database | server should zip it and save it
	bot.send_message(chat_id = update.message.chat_id , text = "Got it. \n⌛️ Saving ... ⌛️")
	sleep(3)
	bot.send_message(chat_id = update.message.chat_id , text = "✅ Successful ✅")
	conLog("Successful")

def send_project_method(bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ send_project_method".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  send_project")
	bot.send_message(chat_id = update.message.chat_id , text = "Ok. Now send me your project !")
	#wait to get data and send them to server or database | server should zip it and save it
	bot.send_message(chat_id = update.message.chat_id , text = "Got it. \n⌛️ Saving ... ⌛️")
	sleep(3)
	bot.send_message(chat_id = update.message.chat_id , text = "✅ Successful ✅")
	conLog("Successful")

def notice_method(bot , update):#need stickers
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ notice".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  notice")
	bot.send_message(chat_id = update.message.chat_id , text = "Alright. What are you going to releaze ???")
	text = "The sent message"
	releazeText = "[{JOB}] {realname} \n\n {text} \n\n {#}{JOB}"#.format(from database by requesting job and nickname)
	bot.send_message(chat_id = update.message.chat_id , text = "That's the preview. Are U sure U want to send it ???")
	#if yes :
	#	bot.send_message(chat_id = group_chat_id , text = releazeText)
	#	else cancel
	#	send the log to the server as success or fail and save the files and increase the sent messages for example

def ping_method(bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ Latency check ...".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  Checking ping ... ")
	system("ping 4.2.2.4")
	ping = "ping of google"
	#ping = system("pint 4.2.2.4")
	bot.send_message(chat_id = update.message.chat_id , text = ping)# how to measure ping in python (the function or the liberrary)

def photo_detecter_test (bot , update):
	bot.send_message(chat_id = "-1001309221311" , text = "{} {} ➡️ sent a picture".format(update.message.from_user.first_name , update.message.from_user.last_name))
	print (update.message.from_user.first_name ," ", update.message.from_user.last_name ," ", update.message.from_user.username , " >>>  sent a picture")
	bot.send_message(chat_id = update.message.chat_id , text = "U have sent me a photo")

def gb_method (bot , update):
	keyboard = [
				InlineKeyboardButton("option 1" , callback_data="1"),
				InlineKeyboardButton("option 2" , callback_data="2"),
				InlineKeyboardButton("option 3" , callback_data="3")
				]
	reply_markup = InlineKeyboardMurkup(keyboard)
	update.message.reply_text("pls choose !" , reply_markup = reply_markup)

def custom_keyboard (bot , update):
	custom_keyboard = [['top-left', 'top-right'], 
                   	   ['bottom-left', 'bottom-right']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(chat_id=chat_id, 
                 text="Custom Keyboard Test", 
                 reply_markup=reply_markup)

def text_AI (bot , update):
	#bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
	text = update.message.text
	print(text)
	if "hi" in update.message.text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
	elif "Hi" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hi 👋")
	elif "hello" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hello 👋")
	elif "Hello" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "Hello 👋")
	elif "slm" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "slm 👋")
	elif "salam" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "salam 👋")
	elif "سلام" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "سلام 👋")
	elif "sghl" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "سلام")

	if "الو" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "جانم ؟")

	if "خوبی" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "سپاسگزارم. شما چطور هستید ؟")
	elif "چطوری" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "عالی. سپاسگزارم. شما چطور هستید ؟")

	if "عالی" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	elif "عالیم" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	elif "خوب" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	elif "خوبم" in text:
		bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	#elif "" in text:
	#	bot.send_message(chat_id = update.message.chat_id , text = "خدارو شکر")
	


#all commands should be closed in group except some interesting and special methods and commands =/
updater.dispatcher.add_handler(CommandHandler('start' , start_method))
updater.dispatcher.add_handler(CommandHandler('help' , help_method))
updater.dispatcher.add_handler(CommandHandler('version' , bot_version_method))
updater.dispatcher.add_handler(CommandHandler('admin' , admin_method))
updater.dispatcher.add_handler(CommandHandler('chat_id' , chat_id_method))
updater.dispatcher.add_handler(CommandHandler('myjob' , my_job_method))
updater.dispatcher.add_handler(CommandHandler('send_activity' , send_activity_method))
updater.dispatcher.add_handler(CommandHandler('send_project' , send_project_method))
updater.dispatcher.add_handler(CommandHandler('notice' , notice_method))#for sending an important message in the group as a formal notification or message | for exaple : masoul fani : U have problem or the check starts at 8:00
#updater.dispatcher.add_handler(CommandHandler('google' , google_method))#should search a phrase in google and show the resault
updater.dispatcher.add_handler(CommandHandler('ping' , ping_method))#It shouldn't be a key =\
updater.dispatcher.add_handler(CommandHandler('latency' , ping_method))#It shouldn't be a key =\
#updater.dispatcher.add_handler(MessageHandler('gb' , gb_method))
#updater.dispatcher.add_handler(MessageHandler('k' , custom_keyboard))
#updater.dispatcher.add_handler(MessageHandler(Filters.photo , photo_detecter_test))
updater.dispatcher.add_handler(MessageHandler(Filters.text , text_AI))

#custom keyboards
#func (start , start)
updater.start_polling()
updater.idle()

#----------PERSONAL DATABASE----------#
#username
#fullname in telegram
#realname
#job
#personal log
#number of sent activities
#number of sent projects
#number of sent messages in group
#number of sent formal notifications
#google search history


#----------DATABASE----------#
#all logs
#number of all sent data and messagess
#google search history


#----------FUTURE DATABASE----------#
#add an event
#add a challenge
#add a purpose
#add some hadis or find the hadises from the enternet


#----------ACTIVITY MEASURING----------#
#sent messages x1 (anti spam should be applied)
#sent notifications or posts x5
#replayed messages x10
#number of messages which contains name of other members x1 fo each name
#number of replies that relates to sent message x10


#----------PACKET STRUCTURE----------#
#Filename = ASCII(Sender or member) + date(based on second) + subject + encryption_method(UIAXETCQ, b, c, ...)
#password