import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CATEGORY, SUBJECT, DESCRIPTION= range(3)
def SendActivity(update, context):
    reply_keyboard = [['Website', 'Android']]

    update.message.reply_text(
        'Select category',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return CATEGORY
def category(update, context):
    user = update.message.from_user
    #logger.info("category of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Ok now write the subject',
                              reply_markup=ReplyKeyboardRemove())

    return SUBJECT
def subject(update, context):
    user = update.message.from_user
    update.message.reply_text('now send me the descriothion')

    return DESCRIPTION
def description(update, context):
    user = update.message.from_user
    user_location = update.message.location
    update.message.reply_text('Thanks the conversation finished')

    return ConversationHandler.END
def cancel(update, context):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
updater = Updater("1017559271:AAG-Rj4fc14ondDY9ABeVfzdK2PkFEMvmhs", use_context=True)

    # Get the dispatcher to register handlers
dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
send_activity_handler = ConversationHandler(
    entry_points=[CommandHandler('send_activity', SendActivity)],

    states={
        CATEGORY: [MessageHandler(Filters.text, category)],#[MessageHandler(Filters.regex('^(Website|Android)$'), category)],

        SUBJECT: [MessageHandler(Filters.text, subject)],

        DESCRIPTION: [MessageHandler(Filters.text, description)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)
dp.add_handler(send_activity_handler)
dp.add_error_handler(error)
updater.start_polling()
updater.idle()
