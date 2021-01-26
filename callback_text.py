from callback import *

dict = {}


def callback_menu(update, context):
    id = update.message.chat_id
    if not id in dict:
        dict[id] = Alram()
    alarm = dict[id]
    # =================================================================
    if update.message.text == "برگشت به منو":
        menu(update, context)

    if update.message.text == "برگشت":
        alarm.stop()
        menu_alert(update)
    # ===================================================================
    if update.message.text == '🔔 آلارم صف خرید':
        alarm.run(alarm.buy_queue, update)

    if update.message.text == '🔔 آلارم صف فروش':
        alarm.run(alarm.sale_queue, update)

    if update.message.text == '🔔 آلارم خرید و فروش گروهی حقیقی':
        alarm.run(alarm.group_buy_sale, update)

    if update.message.text == '🔔 تغییر سرانه خریدار یا فروشنده حقیقی':
        alarm.run(alarm.capita_buy_sale, update)

    if update.message.text == '🔔 خرید و فروش سنگین حقوقی':
        alarm.run(alarm.hoghoghi_buy_sale, update)

    if update.message.text == '🔔 نمایش همه':
        alarm.run(alarm.all_part, update)

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
