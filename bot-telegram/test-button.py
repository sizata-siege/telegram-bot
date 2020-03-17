#in the name of god
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = Updater("919317811:AAHRGZNZIWZS17DXx6NlTQzPl4c_LhPtsWM")
dp = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "Hi /button")

def option(bot, update):
    button = [
        [InlineKeyboardButton("Option 1", callback_data = "1"),
         InlineKeyboardButton("Option 2", callback_data = "2")],
        [InlineKeyboardButton("Option 3", callback_data = "3")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id = update.message.chat_id, text = "Fuck",
                     reply_markup = reply_markup)

startHandler = CommandHandler('start', start)
btHandler = CommandHandler('button', option)

dp.add_handler(startHandler)
dp.add_handler(btHandler)


updater.start_polling()