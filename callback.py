import time

import telegram
from telegram.ext import CallbackContext

from view import DataBase
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def shopp_queue(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if database.is_check_active():
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "وملت", "فولاد", "شستا", "ذوب", "شبدر", "شبدر", "صبا", "وملت",
                "فولاد", "شستا", "ذوب", "وملت", "فولاد", "شستا", "ذوب", "شبدر", "شبدر"]

        for i in list:
            update.message.reply_text('{} صف خرید ✅'.format(i), reply_markup=markup)
            time.sleep(2)
            if stop_event.is_set() or database.is_check_active() == False:
                if database.is_check_active() == False:
                    text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                    update.message.reply_text(text)
                stop_event.clear()
                menu_alert(update)
                break
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


def sale_queue(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if database.is_check_active():
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "شبدر"]

        for i in list:
            update.message.reply_text('{} صف فروش ❌'.format(i), reply_markup=markup)
            time.sleep(1)
            if stop_event.is_set() or database.is_check_active() == False:
                if database.is_check_active() == False:
                    text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                    update.message.reply_text(text)
                stop_event.clear()
                menu_alert(update)
                break
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


def purchase_subscrip(update):
    key = [
        [InlineKeyboardButton(" اشتراک یک ماهه 👍 ", callback_data='اشتراک یک ماهه'),
         InlineKeyboardButton(" اشتراک سه ماهه✊ ", callback_data='اشتراک سه ماهه'), ],
        [InlineKeyboardButton(" اشتراک شیش ماهه💪 ", callback_data='اشتراک شیش ماهه'), ],
    ]
    bttn = InlineKeyboardMarkup(key)
    update.message.reply_text(" لطفاانتخاب کنید👇 ", reply_markup=bttn)


def free_subscription(update):
    text = """برای دریافت اشتراک رایگان شما باید لینک دعوت برای بقیه بفرستید و بعد از عضویت 5 نفر , به شما یک هفته امکان اسفاده از امکانات ربات میده. \n یرای دریافت لینک روی دریافت لینک کلیک کنید""".format(
        update.message.from_user.first_name)

    key = [["دریافت لینک دعوت"], ['نمایش افراد دعوت شده توسط شما'], ['برگشت به منو']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(text, reply_markup=markup)


def queue_alert(update):
    key = [["🔔 آلارم صف خرید", "🔔 آلارم صف فروش"], ['برگشت به منو']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(" لطفا انتخاب کنید ", reply_markup=markup)


def menu_alert(update):
    text = "منو"
    key = [["🔔 آلارم صف خرید", "🔔 آلارم صف فروش"], ['برگشت به منو']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text, reply_markup=markup)


# ======================= Commend ===========================================
def menu(update, context):
    text = "منو"
    key = [["🔔 آلارم صف خرید و فروش"], ["🛒 خرید اشتراک", 'اشتراک رایگان']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text, reply_markup=markup)


def end_subscript(bot, chat_id):
    bot.send_message(chat_id=chat_id, text="اتمام اشتراک")


def start(update, context):
    update = update.message
    key = [["🔔 آلارم صف خرید و فروش"], ["🛒 خرید اشتراک", 'اشتراک رایگان']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)

    database = DataBase(update.chat.first_name, update.chat_id, update.text)
    database.run(context)

    text = """🌹سلام {} عزیز 🌹\nبه ربات تحلیلگر بورس خوش آمدید برای شروع روی منو های مورد نظر کلیک کنید👇""".format(
        update.from_user.first_name)
    update.reply_text(text, reply_markup=markup)


def link(update, context):
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
