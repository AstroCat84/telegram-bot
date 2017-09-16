from telegram.ext import Updater, CommandHandler

def start(bot, update): #Replies 'Hello World' as a reply to /start
    update.message.reply_text('Hello World!')

def hello(bot, update): #Replies 'Hello {User first name} as a reply to /hello'
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('your API key')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
