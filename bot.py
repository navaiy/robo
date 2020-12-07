#!/usr/bin/env python3
import _thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from callback_query import *
from callback_text import *
from model import UserInfo, session

proxy = {'proxy_url': 'http://127.0.0.1:13093/'}

main_token = '1485237615:AAHIguavJ44PfFOEnn7Vnn8CBQeO0lWyESo'
second_token = '1216019804:AAEnT-e_6rMrN8vnnutpx_TlJbzEX2oY2Ok'
updater = Updater(second_token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('link', link))
updater.dispatcher.add_handler(CommandHandler('menu', menu))
updater.dispatcher.add_handler(CommandHandler('list_invite', list_invite))

updater.dispatcher.add_handler(CallbackQueryHandler(query))
updater.dispatcher.add_handler(MessageHandler(Filters.text, callback_menu))


# Check subscription time


def check_time():
    while True:
        user = session.query(UserInfo).all()
        for i in user:
            if i.time_active > 0:
                i.time_active -= 1
                session.commit()
        session.close()
        time.sleep(60)


_thread.start_new_thread(check_time, ())

updater.start_polling()
updater.idle()
