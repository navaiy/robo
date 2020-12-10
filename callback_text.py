import threading
from threading import Thread
from callback import *

stop_event = threading.Event()


def callback_menu(update, context):
    if update.message.text == "برگشت به منو":
        menu(update, context)

    if update.message.text == "برگشت":
        stop_event.set()
        menu_alert(update)
    # ===================================================================
    if update.message.text == '🔔 آلارم صف خرید':
        Thread(target=shopp_queue, args=(update, stop_event)).start()

    if update.message.text == '🔔 آلارم صف فروش':
        Thread(target=sale_queue, args=(update, stop_event)).start()
    # ===================================================================
    if update.message.text == "🔔 آلارم صف خرید و فروش":
        queue_alert(update)

    if update.message.text == "🛒 خرید اشتراک":
        purchase_subscrip(update)

    if update.message.text == "اشتراک رایگان":
        free_subscription(update)
    # =====================================================================================
    if update.message.text == "دریافت لینک دعوت":
        link(update, context)

    if update.message.text == "نمایش افراد دعوت شده توسط شما":
        list_invite(update, context)
