from time import sleep

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from model_alarm import SaleQueue, session, GroupBuySale, BuyQueue, CapitaBuySale, HoghoghiBuySale

# ======================== part ==========================
# صف خرید در حال ریختن
from view import DataBase


def buy_queue(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if True:  # database.is_check_active()
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        # list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "وملت", ]
        while True:
            text = "🔔❌ کاهش 50 درصد #صف_خرید ❌🔔\n"
            list = session.query(BuyQueue).all()
            session.close()
            for i in list:
                text += f"""
                        ####################
#{i.symbol}
حجم صف خرید قدیم : {i.old_queue}
حجم صف خرید جدید : {i.new_queue}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
            if stop_event.is_set():  # or database.is_check_active() == False
                # if database.is_check_active() == False:
                #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                #     update.message.reply_text(text)
                stop_event.clear()
                break
            update.message.reply_text(text,ParseMode.HTML, reply_markup=markup)
            sleep(0.9)
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


# صف فروش در حال ریختن
def sale_queue(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if True:  # database.is_check_active()
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        # list = ["صبا", "وملت", "فولاد", "شستا", "ذوب", "وملت", "فولاد", "شستا", "صبا", "وملت", "فولاد", "شستا", "ذوب",
        #         "وملت", "فولاد", "شستا", "ذوب", "ذوب", "صبا", "وملت", "فولاد", "شستا", "ذوب", "وملت", "فولاد", "شستا",
        #         "صبا", "وملت", "فولاد", "شستا", "ذوب"]

        while True:
            text = "🔔✅ کاهش 20 درصدی #صف_فروش ✅🔔\n"
            list = session.query(SaleQueue).all()
            session.close()
            for i in list:
                text += f"""
                        ####################
#{i.symbol}
حجم صف فروش قدیم : {i.old_queue}
حجم صف فروش جدید : {i.new_queue}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
            if stop_event.is_set():  # or database.is_check_active() == False
                # if database.is_check_active() == False:
                #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                #     update.message.reply_text(text)
                stop_event.clear()
                session.close()
                break
            sleep(0.9)
            update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


# خرید و فروش گروهی
def group_buy_sale(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if True:  # database.is_check_active()
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        # list = ["صبا", "وملت", "فولاد", "شستا", ]

        while True:
            text = "🔔 خرید و فروش گروهی حقیقی 🔔\n"
            list = session.query(GroupBuySale).all()
            session.close()
            for i in list:
                text += f"""
                    ####################
وضعیت {i.status} برای نماد #{i.symbol}
تعداد {i.status}  : {i.number_buy_or_sale}
هر کد حقیقی : {i.each_haghighi}
ارزش {i.status} : {i.value_buy_or_sale}
قیمت معامله : {i.price_and_percentage}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
            if stop_event.is_set():  # or database.is_check_active() == False
                # if database.is_check_active() == False:
                #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                #     update.message.reply_text(text)
                stop_event.clear()

                break
            update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
            sleep(0.9)
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


# تغییر سرانه خریدار یا فروشنده حقیقی
def capita_buy_sale(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if True:  # database.is_check_active()
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        # list = ["صبا", "وملت", "فولاد", "شستا", ]
        while True:
            list = session.query(CapitaBuySale).all()
            session.close()
            text = "🔔 تغییر سرانه خریدار یا فروشنده حقیقی 🔔\n"
            for i in list:
                text += f"""
                    ####################
وضعیت سرانه {i.status} برای نماد #{i.symbol}
سرانه خریدار قدیم  : {i.old_buy}
سرانه فروشنده قدیم : {i.old_sale}
سرانه خریدار جدید : {i.new_buy}
سرانه فروشنده جدید : {i.new_sale}
درصد تغییر سرانه خریدار به فروشنده : {i.percentage_change_buy_sale}
قیمت معامله و درصد : {i.percentage_change}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
            if stop_event.is_set():  # or database.is_check_active() == False
                # if database.is_check_active() == False:
                #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                #     update.message.reply_text(text)
                stop_event.clear()
                break
            update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
            sleep(0.9)
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


# خرید و فروش سنگین حقوقی
def hoghoghi_buy_sale(update, stop_event):
    database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
    if True:  # database.is_check_active()
        key = [["برگشت"]]
        markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
        # list = ["صبا", "وملت", "فولاد", "شستا", ]
        while True:
            list = session.query(HoghoghiBuySale).all()
            session.close()
            text = "🔔 خرید و فروش سنگین حقوقی 🔔\n"
            for i in list:
                text += f"""
                    ####################
وضعیت {i.status} برای نماد #{i.symbol}
ارزش {i.status} : {i.value_buy_or_sale}
قیمت معامله و درصد : {i.price_and_percentage}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
            if stop_event.is_set():  # or database.is_check_active() == False
                # if database.is_check_active() == False:
                #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                #     update.message.reply_text(text)
                stop_event.clear()

                break
            update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
            sleep(0.9)
    else:
        text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
        update.message.reply_text(text)


# ==================================================
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
    key = [["🔔 آلارم صف خرید", "🔔 آلارم صف فروش"], ['🔔 تغییر سرانه خریدار یا فروشنده حقیقی'],
           ['🔔 آلارم خرید و فروش گروهی حقیقی'], ['🔔 خرید و فروش سنگین حقوقی'], ['برگشت به منو']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(" لطفا انتخاب کنید ", reply_markup=markup)


def menu_alert(update):
    text = "منو"
    key = [["🔔 آلارم صف خرید", "🔔 آلارم صف فروش"], ['🔔 تغییر سرانه خریدار یا فروشنده حقیقی'],
           ['🔔 آلارم خرید و فروش گروهی حقیقی'], ['🔔 خرید و فروش سنگین حقوقی'], ['برگشت به منو']]
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
