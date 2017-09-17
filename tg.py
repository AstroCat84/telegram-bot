from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def echo(bot, update): #Replies 'Hello World' as a reply to /start
    update.message.reply_text(update.message.text)

def hello(bot, update): #Replies 'Hello {User first name} as a reply to /hello'
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def main():

    updater = Updater('448790793:AAGq7aTyr2VmXTlu6R4pK3VMUSEPoAqfX80')


    updater.dispatcher.add_handler(CommandHandler('echo', echo))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
