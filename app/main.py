import logging
from telegram.ext import Updater, CommandHandler

updater = Updater(token="766069214:AAGl3z19mqIGBgtjTddc8Ie5meFhnOVQH50",
                  request_kwargs={'proxy_url': "http://vpn:Amaru42mesike!@91.218.231.38:3128"})
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start_callback(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, my Lord")


start_handler = CommandHandler("start", start_callback)
dispatcher.add_handler(start_handler)
updater.start_polling()
