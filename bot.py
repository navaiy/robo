#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from query import *
from callback_text import *

proxy = {'proxy_url': 'http://127.0.0.1:13093/'}

main_token = '1485237615:AAHIguavJ44PfFOEnn7Vnn8CBQeO0lWyESo'
second_token = '1216019804:AAEnT-e_6rMrN8vnnutpx_TlJbzEX2oY2Ok'
updater = Updater(second_token)

updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('link', link))
# updater.dispatcher.add_handler(CommandHandler('menu', menu))
# updater.dispatcher.add_handler(CommandHandler('list_invite', list_invite))
#
# updater.dispatcher.add_handler(CallbackQueryHandler(query))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, callback_menu))

updater.start_polling()
updater.idle()
