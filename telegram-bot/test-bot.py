from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

Token = "1017559271:AAG-Rj4fc14ondDY9ABeVfzdK2PkFEMvmhs"
updater = Updater(token=Token, use_context=True)
dp = updater.dispatcher


def get_owner(update, context):
    admins = context.bot.get_chat_administrators(chat_id=update.effective_chat.id)
    for admin in admins:
        if admin.status == 'creator':
            return admin

def start(update, context):
    keyboard = [
        [InlineKeyboardButton('Test', callback_data='test')]
    ]
    test_markup = InlineKeyboardMarkup(keyboard)
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="Hi\n\nhttp://t.me/sizata_test_bot?startgroup=new", reply_markup=test_markup)
    print(update)
    print(get_owner(update, context))
    # admins = context.bot.get_chat_administrators(chat_id=update.effective_chat.id)
    # print(admins)
    # # print(admins[1])
    # for admin in admins:
    #     print(admin)

def cq(update, context):
    print(update)
    print(update.effective_user)
    print(context.bot)

def msg(update, context):
    print()
    print(update)
    print(update.effective_user)
    print(update.effective_chat)
    print(update.effective_message)
    if update.effective_message.edit_date:
        print('edited')


start_handler = CommandHandler('start', start)
cq_handler = CallbackQueryHandler(cq)
message_handler = MessageHandler(Filters.text, msg)

dp.add_handler(start_handler)
dp.add_handler(cq_handler)
dp.add_handler(message_handler)

updater.start_polling()
updater.idle()
