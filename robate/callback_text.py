import random
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from robate.callback import *

stop = False


def callback_menu(update, context):
    def sa():
        print(update)

    if update.message.text == "برگشت به منو":
        menu(update, context)

    # ===================================================================
    if update.message.text == '🔔 آلارم صف خرید':
        database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if database.is_check_active():
            key = [["برگشت به منو"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "شبدر"]
            for i in list:
                # print(query)
                update.message.reply_text('{} صف خرید ✅'.format(i), reply_markup=markup)
                time.sleep(random.randrange(1, 4))
                sa()
        else:
            update.message.reply_text(
                'شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید \n  برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید')

    if update.message.text == '🔔 آلارم صف فروش':
        database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if database.is_check_active():
            key = [["برگشت به منو"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "شبدر"]
            for i in list:
                # print(query)
                update.message.reply_text('{} صف خرید ❌'.format(i), reply_markup=markup)
                time.sleep(random.randrange(1, 4))
                sa()
        else:
            update.message.reply_text(
                'شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید \n  برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید')

    # ===================================================================
    if update.message.text == "🔔 آلارم صف خرید و فروش":
        key = [["🔔 آلارم صف خرید", "🔔 آلارم صف فروش"], ['برگشت به منو']]
        markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(" لطفا انتخاب کنید ", reply_markup=markup)

    if update.message.text == "🛒 خرید اشتراک":
        key = [
            [InlineKeyboardButton(" اشتراک یک ماهه 👍 ", callback_data='اشتراک یک ماهه'),
             InlineKeyboardButton(" اشتراک سه ماهه✊ ", callback_data='اشتراک سه ماهه'), ],
            [InlineKeyboardButton(" اشتراک شیش ماهه💪 ", callback_data='اشتراک شیش ماهه'), ],
        ]
        bttn = InlineKeyboardMarkup(key)
        update.message.reply_text(" لطفاانتخاب کنید👇 ", reply_markup=bttn)

    if update.message.text == "اشتراک رایگان":
        text = """برای دریافت اشتراک رایگان شما باید لینک دعوت برای بقیه بفرستید و بعد از عضویت 5 نفر , به شما یک هفته امکان اسفاده از امکانات ربات میده. \n یرای دریافت لینک روی دریافت لینک کلیک کنید""".format(
            update.message.from_user.first_name)

        key = [["دریافت لینک دعوت"], ['نمایش افراد دعوت شده توسط شما'], ['برگشت به منو']]
        markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)

        update.message.reply_text(text, reply_markup=markup)
    # =====================================================================================
    if update.message.text == "دریافت لینک دعوت":
        link(update, context)

    if update.message.text == "نمایش افراد دعوت شده توسط شما":
        list_invite(update, context)
