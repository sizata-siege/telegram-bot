#IN THE NAME OF GOD

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters#, MessageEntity 
Token = "919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM"
updater = Updater(token = Token, use_context = True)
dp = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

text = "Hi"

def start_method(update, context):
    update.message.reply_text("Welcome to my awesome bot!")
    print(context)
    print(update.message)
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!\n/test")
    
def callback(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hi")

start_handler = CommandHandler('start', start_method)
dp.add_handler(start_handler)
# dp.add_handler(CommandHandler('test', tst))
handler = MessageHandler(Filters.forwarded, callback)
dp.add_handler(handler)

updater.start_polling()
updater.idle()