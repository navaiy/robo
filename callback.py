from view import DataBase
from telegram import ReplyKeyboardMarkup


def menu(update, context):
    text = "منو"
    key = [["🔔 آلارم صف خرید و فروش"], ["🛒 خرید اشتراک", 'اشتراک رایگان']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text, reply_markup=markup)


def start(update, context, ):
    update = update.message
    key = [["🔔 آلارم صف خرید و فروش"], ["🛒 خرید اشتراک", 'اشتراک رایگان']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)

    database = DataBase(update.chat.first_name, update.chat_id, update.text)
    database.run(context)

    text = """🌹سلام {} عزیز 🌹\nبه ربات تحلیلگر بورس خوش آمدید برای شروع روی منو های مورد نظر کلیک کنید👇""".format(
        update.from_user.first_name)
    update.reply_text(text, reply_markup=markup)


def link(update, context, ):
    link = "https://t.me/sdsdfd_bot?start={}".format(update.message.chat_id)
    text = """سلام من ربات تحلیلگر بورسم برای مطلع شدن از صف های خرید و فروش بر روی لینک زیر کلیک کنید \n {}""".format(
        link, update.message.from_user.first_name)
    update.message.reply_text(text)


def list_invite(update, context):
    update = update.message
    database = DataBase(update.chat.first_name, update.chat_id, update.text)
    text = database.get_list_invited()
    # print(text)
    if text == "":
        text = "هنوز هیچ فردی از طریق شما دعوت نشده 😢"
    update.reply_text(text)
