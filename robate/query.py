import random
import time
from .callback_text import *
from telegram import ReplyKeyboardMarkup


def query(update, context):
    query = update.callback_query
    # ===================================================================
    if query.data == 'صف خرید':
        key = [["برگشت به منو"]]
        markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
        list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "شبدر"]
        for i in list:
            # print(query)
            print(update.message.text)
            time.sleep(random.randrange(1, 4))
            # callback_menu(update, context)
            context.bot.send_message(query.message.chat_id, '{} صف خرید ✅'.format(i), reply_markup=markup)
    if query.data == 'صف فروش':
        key = [["برگشت به منو"]]
        markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
        list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "شبدر"]
        for i in list:
            time.sleep(random.randrange(1, 4))
            context.bot.send_message(query.message.chat_id, '{} صف فروش ❌'.format(i), reply_markup=markup)
    # ================================================================================
    if query.data == "اشتراک یک ماهه":
        context.bot.send_message(query.message.chat_id, 'اشتراک یک ماهه')
    if query.data == "اشتراک سه ماهه":
        context.bot.send_message(query.message.chat_id, 'اشتراک سه ماهه')
    if query.data == "اشتراک شیش ماهه":
        context.bot.send_message(query.message.chat_id, 'اشتراک شیش ماهه')
