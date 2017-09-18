#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is under the MIT license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def echo(bot, update): #Replies 'Hello World' as a reply to /start
    update.message.reply_text(update.message.text)

def hello(bot, update): #Replies 'Hello {User first name} as a reply to /hello'
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def main():

    updater = Updater('TOKEN')


    updater.dispatcher.add_handler(CommandHandler('echo', echo))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
