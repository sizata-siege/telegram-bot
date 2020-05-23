# IN THE NAME OF GOD
# The keyboards and markups will be placed here
# Complete all keyboards and their markups
# use panel or start ?

# ------------------------------ Modules ------------------------------ #
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, replykeyboardmarkup, replykeyboardremove

# ------------------------------ InlineKeyboards ------------------------------ #
newcomer_start_inline_en_s = [
    [InlineKeyboardButton("")]
]
nsies_markup = InlineKeyboardMarkup(newcomer_start_inline_en_s)

user_start_inline_en_s = [
    [InlineKeyboardButton("📈 My Activity 📈", callback_data="my_stats")],
    [InlineKeyboardButton("📊 Scoreboard 📊", callback_data="scores")],
    [InlineKeyboardButton("👑 My Rank 👑", callback_data="my_rank"),
     InlineKeyboardButton("Ranking System", callback_data="ranking_system")],
    [InlineKeyboardButton("Send Activity", callback_data="send_activity")],
    [InlineKeyboardButton("Send Project", callback_data="send_project")],
    [InlineKeyboardButton("Report BUGs & Problems", callback_data="report_bug")],
    ...
]
usies_markup = InlineKeyboardMarkup(user_start_inline_en_s)

user_start_inline_en = [
    # without stickers depending on manager choices
]
usie_markup = InlineKeyboardMarkup(user_start_inline_en)

user_start_inline_fa_s = []
usifs_markup = InlineKeyboardMarkup(user_start_inline_fa_s)

user_start_inline_fa = []
usif_markup = InlineKeyboardMarkup(user_start_inline_fa)

customer_start_inline_en_s = [
    [InlineKeyboardButton("Reservation", callback_data="reservation")],
    [...]
]

customer_start_inline_en = []

admin_start_inline_en_s = []

admin_start_inline_en = []

admin_start_inline_fa_s = []

admin_start_inline_fa = []

new_group_start_inline_en = [
    [InlineKeyboardButton("Register in Website", callback_data="register_in_website")],
    [InlineKeyboardButton("Register in Telegram", callback_data="register_in_telegram")],
    [InlineKeyboardButton("Free Trial in Website", callback_data="free_trial_in_website")],
    [InlineKeyboardButton("Free Trial in Telegram", callback_data="free_trial_in_telegram")]  # How to open a link in a button
]

# ------------------------------ ReplyKeyboards ------------------------------ #



# ------------------------------ Panel text ------------------------------ #
newcomer_panel_en = "You aren't registered yet.\n\nIf you are a group owner, add the bot to your group to start the service.\n\nhttp://t.me/activity_monitoring_bot?startgroup=new\n\nOfficial website :\nhttps://activity-monitoring.ir"
newcomer_panel_fa = "شما هنوز در ربات ثبت نام نشده/نکرده اید\n\nاگر گروهی دارید، میتوانید با افزودن ربات به گروه خود از طریق لینک زیر از خدمات ربات استفاده کنید\n\nhttp://t.me/activity_monitoring_bot?startgroup=new"
owner_panel_en = "Welcome back %s \n\nWhat do you want to do?"
owner_panel_fa = "خوش آمدید. \n\nچه چیزی در سر دارید؟"
assistant_panel_en = "Hi %s 👋\n\nHow is everything?"
user_panel_en = "Hi %s 👋.\n\nYour current score was %s"

new_group_panel_en = "This group is not registered yet.\n\nUse the link below to register your group or use free trial.\n\nRegisteration ➡️ https://activity_monitoring.ir/registeration\nFree Trial ➡️ https://activity_monitoring.ir/free_trial"
group_start_trial = "✅ Bot Started ✅\n%s members detected\nAll messages will affect users activities\n"
