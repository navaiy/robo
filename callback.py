import time
from threading import Thread, Event
from time import sleep

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from model_alarm import SaleQueue, session, GroupBuySale, BuyQueue, CapitaBuySale, HoghoghiBuySale
from view import DataBase


# ======================== part ==========================
class Alram:
    t_e = 12 * 3600 + 30 * 60
    t_s = 9 * 3600

    def __init__(self):
        self.stop_event = Event()

    def stop(self):
        self.stop_event.set()
        sleep(1.5)
        self.stop_event.clear()

    def run(self, fun, update):
        t_n = time.localtime().tm_hour * 3600 + time.localtime().tm_min * 60 + time.localtime().tm_sec
        if self.t_s < t_n and self.t_e > t_n:
            Thread(target=fun, args=(update,)).start()
        else:
            markup = ReplyKeyboardMarkup([["برگشت"]], resize_keyboard=True)
            update.message.reply_text("وقت بازار تموم شده لطفا بعدا در وقت بازار استفاده کنید.", ParseMode.HTML,
                                      reply_markup=markup)

    def check_open_market(self, update):
        t_n = time.localtime().tm_hour * 3600 + time.localtime().tm_min * 60 + time.localtime().tm_sec
        if not self.t_e > t_n:
            markup = ReplyKeyboardMarkup([["برگشت"]], resize_keyboard=True)
            update.message.reply_text("وقت بازار تموم شده لطفا بعدا در وقت بازار استفاده کنید.", reply_markup=markup)
            return True

        if self.stop_event.is_set():
            self.stop_event.clear()
            return True
        return False

    # صف خرید در حال ریختن
    def buy_queue(self, update):
        # database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if True:  # database.is_check_active()
            key = [["برگشت"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            update.message.reply_text("لطفا صبر کنید...", ParseMode.HTML, reply_markup=markup)
            last_new = session.query(BuyQueue).count()
            while True:
                if self.check_open_market(update):
                    break
                text = "🔔❌ کاهش 50 درصد #صف_خرید ❌🔔\n"
                last_old = last_new
                sleep(1)
                last_new = session.query(BuyQueue).count()
                if last_old < last_new:
                    list = session.query(BuyQueue).all()[last_old:]
                    for i in list:
                        text += f"""
                                ####################
#{i.symbol}
حجم صف خرید قدیم :{i.old_queue}
حجم صف خرید جدید :{i.new_queue}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if self.stop_event.is_set():  # or database.is_check_active() == False
                        # if database.is_check_active() == False:
                        #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                        #     update.message.reply_text(text)
                        self.stop_event.clear()
                        break
                    else:
                        update.message.reply_text(text, ParseMode.HTML, reply_markup=markup)
                session.close()
        else:
            text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
            update.message.reply_text(text)

    # صف فروش در حال ریختن
    def sale_queue(self, update):
        # database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if True:  # database.is_check_active()
            key = [["برگشت"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            update.message.reply_text("لطفا صبر کنید...", ParseMode.HTML, reply_markup=markup)
            last_new = session.query(SaleQueue).count()
            while True:
                if self.check_open_market(update):
                    break
                text = "🔔✅ کاهش 20 درصدی #صف_فروش ✅🔔\n"
                last_old = last_new
                sleep(1)
                last_new = session.query(SaleQueue).count()
                if last_old < last_new:
                    list = session.query(SaleQueue).all()[last_old:]
                    for i in list:
                        text += f"""
                                ####################
#{i.symbol}
حجم صف فروش قدیم :{i.old_queue}
حجم صف فروش جدید :{i.new_queue}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if self.stop_event.is_set():  # or database.is_check_active() == False
                        # if database.is_check_active() == False:
                        #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                        #     update.message.reply_text(text)
                        self.stop_event.clear()
                        break
                    else:
                        update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)

                session.close()
        else:
            text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
            update.message.reply_text(text)

    # خرید و فروش گروهی
    def group_buy_sale(self, update):
        # database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if True:  # database.is_check_active()
            key = [["برگشت"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            update.message.reply_text("لطفا صبر کنید...", ParseMode.HTML, reply_markup=markup)
            last_new = session.query(GroupBuySale).count()
            while True:
                if self.check_open_market(update):
                    break
                last_old = last_new
                sleep(1)
                last_new = session.query(GroupBuySale).count()
                text = "🔔 خرید و فروش گروهی حقیقی 🔔\n"
                if last_old < last_new:
                    list = session.query(GroupBuySale).all()[last_old:]
                    for i in list:
                        text += f"""
                            ####################
وضعیت{i.status} برای نماد #{i.symbol}
تعداد{i.status}  : {i.number_buy_or_sale}
هر کد حقیقی :{i.each_haghighi}
ارزش{i.status} : {i.value_buy_or_sale}
قیمت معامله :{i.price_and_percentage}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if self.stop_event.is_set():  # or database.is_check_active() == False
                        # if database.is_check_active() == False:
                        #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                        #     update.message.reply_text(text)
                        self.stop_event.clear()
                        break
                    else:
                        update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
                session.close()

        else:
            text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
            update.message.reply_text(text)

    # تغییر سرانه خریدار یا فروشنده حقیقی
    def capita_buy_sale(self, update):
        # database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if True:  # database.is_check_active()
            key = [["برگشت"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            update.message.reply_text("لطفا صبر کنید...", ParseMode.HTML, reply_markup=markup)
            last_new = session.query(CapitaBuySale).count()
            while True:
                if self.check_open_market(update):
                    break
                last_old = last_new
                sleep(1)
                last_new = session.query(CapitaBuySale).count()
                text = "🔔 تغییر سرانه خریدار یا فروشنده حقیقی 🔔\n"
                if last_old < last_new:
                    list = session.query(CapitaBuySale).all()[last_old:]
                    for i in list:
                        text += f"""
                            ####################
وضعیت سرانه{i.status} برای نماد #{i.symbol}
سرانه خریدار قدیم  :{i.old_buy}
سرانه فروشنده قدیم :{i.old_sale}
سرانه خریدار جدید :{i.new_buy}
سرانه فروشنده جدید :{i.new_sale}
درصد تغییر سرانه خریدار به فروشنده :{i.percentage_change_buy_sale}
قیمت معامله و درصد :{i.percentage_change}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if self.stop_event.is_set():  # or database.is_check_active() == False
                        # if database.is_check_active() == False:
                        #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                        #     update.message.reply_text(text)
                        self.stop_event.clear()
                        break
                    else:
                        update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)

                session.close()

        else:
            text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
            update.message.reply_text(text)

    # خرید و فروش سنگین حقوقی
    def hoghoghi_buy_sale(self, update):
        # database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if True:  # database.is_check_active()
            key = [["برگشت"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            update.message.reply_text("لطفا صبر کنید...", ParseMode.HTML, reply_markup=markup)
            last_new = session.query(HoghoghiBuySale).count()
            while True:
                if self.check_open_market(update):
                    break
                text = "🔔 خرید و فروش سنگین حقوقی 🔔\n"
                last_old = last_new
                sleep(1)
                last_new = session.query(HoghoghiBuySale).count()
                if last_old < last_new:
                    list = session.query(HoghoghiBuySale).all()[last_old - 1:]
                    for i in list:
                        text += f"""
                            ####################
وضعیت{i.status} برای نماد #{i.symbol}
ارزش{i.status} : {i.value_buy_or_sale}
قیمت معامله و درصد :{i.price_and_percentage}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if self.stop_event.is_set():  # or database.is_check_active() == False
                        # if database.is_check_active() == False:
                        #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                        #     update.message.reply_text(text)
                        self.stop_event.clear()
                        break
                    else:
                        update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)

                session.close()
        else:
            text = "شما به دلیل فعال نبودن اشتراک اجازه استفاده ندارید برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
            update.message.reply_text(text)

    # نمایش کل
    def all_part(self, update):

        # database = DataBase(update.message.chat.first_name, update.message.chat_id, update.message.text)
        if True:  # database.is_check_active()
            key = [["برگشت"]]
            markup = ReplyKeyboardMarkup(key, resize_keyboard=True)
            update.message.reply_text("لطفا صبر کنید...", ParseMode.HTML, reply_markup=markup)

            def check(text):
                if self.stop_event.is_set():  # or database.is_check_active() == False
                    # if database.is_check_active() == False:
                    #     text = "متاسفانه اشتراک شما تموم شد. برای فعال کردن میتوانتد اشتراک بخرید با دوستانتون را دعوت کنید"
                    #     update.message.reply_text(text)
                    self.stop_event.clear()
                    return True
                else:
                    update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
                    sleep(0.1)
                return False

            HoghoghiBuySale_new = session.query(HoghoghiBuySale).count()
            BuyQueue_new = session.query(BuyQueue).count()
            SaleQueue_new = session.query(SaleQueue).count()
            GroupBuySale_new = session.query(GroupBuySale).count()
            CapitaBuySale_new = session.query(CapitaBuySale).count()

            while True:
                if self.check_open_market(update):
                    break
                # =======================================
                HoghoghiBuySale_old = HoghoghiBuySale_new
                BuyQueue_old = BuyQueue_new
                SaleQueue_old = SaleQueue_new
                GroupBuySale_old = GroupBuySale_new
                CapitaBuySale_old = CapitaBuySale_new
                sleep(0.9)
                HoghoghiBuySale_new = session.query(HoghoghiBuySale).count()
                BuyQueue_new = session.query(BuyQueue).count()
                SaleQueue_new = session.query(SaleQueue).count()
                GroupBuySale_new = session.query(GroupBuySale).count()
                CapitaBuySale_new = session.query(CapitaBuySale).count()
                # =============================================
                text = "🔔 خرید و فروش سنگین حقوقی 🔔\n"
                if HoghoghiBuySale_old < HoghoghiBuySale_new:
                    list = session.query(HoghoghiBuySale).all()[HoghoghiBuySale_old:]
                    for i in list:
                        text += f"""
                            ####################
وضعیت {i.status} برای نماد #{i.symbol}
ارزش{i.status} : {i.value_buy_or_sale}
قیمت معامله و درصد :{i.price_and_percentage}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if check(text):
                        break
                # ==========================================
                text = "🔔❌ کاهش 50 درصد #صف_خرید ❌🔔\n"
                if BuyQueue_old < BuyQueue_new:
                    list = session.query(BuyQueue).all()[BuyQueue_old:]
                    for i in list:
                        text += f"""
                                    ####################
#{i.symbol}
حجم صف خرید قدیم :{i.old_queue}
حجم صف خرید جدید :{i.new_queue}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if check(text):
                        break
                # ============================================
                text = "🔔✅ کاهش 20 درصدی #صف_فروش ✅🔔\n"
                if SaleQueue_old < SaleQueue_new:
                    list = session.query(SaleQueue).all()[SaleQueue_old:]
                    for i in list:
                        text += f"""
                                ####################
#{i.symbol}
حجم صف فروش قدیم :{i.old_queue}
حجم صف فروش جدید :{i.new_queue}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if check(text):
                        break
                # ==========================================
                text = "🔔 خرید و فروش گروهی حقیقی 🔔\n"
                if GroupBuySale_old < GroupBuySale_new:
                    list = session.query(GroupBuySale).all()[GroupBuySale_old:]
                    for i in list:
                        text += f"""
                                        ####################
وضعیت {i.status} برای نماد #{i.symbol}
تعداد {i.status}  : {i.number_buy_or_sale}
هر کد حقیقی :{i.each_haghighi}
ارزش{i.status} : {i.value_buy_or_sale}
قیمت معامله :{i.price_and_percentage}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    # update.message.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=markup)
                    if check(text):
                        break
                # ==========================================
                text = "🔔 تغییر سرانه خریدار یا فروشنده حقیقی 🔔\n"
                if CapitaBuySale_old < CapitaBuySale_new:
                    list = session.query(CapitaBuySale).all()[CapitaBuySale_old:]
                    for i in list:
                        text += f"""
                                        ####################
وضعیت سرانه {i.status} برای نماد #{i.symbol}
سرانه خریدار قدیم  :{i.old_buy}
سرانه فروشنده قدیم :{i.old_sale}
سرانه خریدار جدید :{i.new_buy}
سرانه فروشنده جدید :{i.new_sale}
درصد تغییر سرانه خریدار به فروشنده :{i.percentage_change_buy_sale}
قیمت معامله و درصد :{i.percentage_change}
<a href='{i.link}'>صفحه در وبسایت تالار بورس</a>
🕘 {i.time}"""
                    if check(text):
                        break
                session.close()
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
           ['🔔 آلارم خرید و فروش گروهی حقیقی'], ['🔔 خرید و فروش سنگین حقوقی'], ['🔔 نمایش همه'], ['برگشت به منو']]
    markup = ReplyKeyboardMarkup(key, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(" لطفا انتخاب کنید ", reply_markup=markup)


def menu_alert(update):
    text = "منو"
    key = [["🔔 آلارم صف خرید", "🔔 آلارم صف فروش"], ['🔔 تغییر سرانه خریدار یا فروشنده حقیقی'],
           ['🔔 آلارم خرید و فروش گروهی حقیقی'], ['🔔 خرید و فروش سنگین حقوقی'], ['🔔 نمایش همه'], ['برگشت به منو']]
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
