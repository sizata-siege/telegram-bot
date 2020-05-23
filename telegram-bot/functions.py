from keyboards import *
from bot_classes import *
from telegram import InlineKeyboardMarkup, ChatAction, ParseMode, MessageEntity

def fetch_user(update):  # check if the update is none and then place the dict equal to none and the check in the other functions
    user = {
        'chat_id': update.effective_chat.id,
        'username': update.effective_user.username,  # update.effective_user.sth
        'first_name': update.effective_user.first_name,
        'last_name': update.effective_user.last_name,
        'is_group': False if update.effective_chat.type == 'private' else True,  # update.message.chat.type
        'text': update.effective_message.text,
        'words': update.effective_message.text.count(' ') + 1,
    }
    return user

def get_admins(update, context):
    return context.bot.get_chat_administrators(chat_id=update.effective_chat.id)

def get_owner(update, context):
    admins = context.bot.get_chat_administrators(chat_id=update.effective_chat.id)
    for admin in admins:
        if admin.status == 'creator':
            return admin

def get_posts(update, context):  # returns a list of chat_id s and posts (custom titles)
    members = context.bot.get_chat_administrators(chat_id=update.effective_chat.id)
    posts = []
    for member in members:
        if member.custom_title:
            tmp_chat_id = member.user.id
            tmp_post = member.custom_title
            posts.append({tmp_chat_id: tmp_post})
    return posts


# -------------------- Bot functions --------------------- #
def start(update, context):  # check the update not None
    ud = fetch_user(update)  # fetch user data
    if not ud['is_group']:  # if bot started in pv
        current_user = User(ud['chat_id'], ud['username'], ud['first_name'], ud['last_name'])  # current user
        if current_user.is_registered():  # if the user is registered ?
            context.bot.send_message(chat_id=ud['chat_id'], text=user_panel_en, reply_markup=usies_markup)
        else:
            context.bot.send_message(chat_id=ud['chat_id'], text=newcomer_panel_en, reply_markup=nsies_markup)  # newcomer panel
    elif ud['is_group']:  # if the bot started in group
        current_group = Group(update.effective_chat.title, get_owner(update, context), update.effective_chat.id)
        if current_group.is_registered():# if the group is registered ?
            current_user = User(ud['chat_id'], ud['username'], ud['first_name'], ud['last_name'])  # current user
            if current_user.is_owner():# if yes then check if the user is owner or assistant ?
                context.bot.send_message(chat_id=ud['chat_id'], text=)# if yes then send the start tracking message and log the chat_id in the file
        # if no then send the access denied message or you don't have permission to do that
        # if no then send the registration guide and log the chat_id in the file
    else:
        pass
        # the update is null so

def admin(update, context):
    ud = fetch_user(update)
    if not ud['is_group']:
        current_user = User(ud['chat_id'], ud['username'], ud['first_name'], ud['last_name'])  # current user
        if current_user.is_registered():  # if the user is registered ?
            if current_user.is_owner():  # if the registered user is an owner or manager ?  # owner panel
                context.bot.send_message(chat_id=ud['chat_id'], text=owner_panel_fa)
            elif current_user.is_assistant():  # show the manager panel or
                context.bot.send_message(chat_id=ud['chat_id'], text=assistant_panel_en)
            else:
                context.bot.send_message(chat_id=ud['chat_id'], text="❌You are not Admin❌")
        else:
            context.bot.send_message(chat_id=ud['chat_id'], text=newcomer_panel_en, reply_markup=nsies_markup)
    else:
        context.bot.send_message(chat_id=ud['chat_id'], text=)
