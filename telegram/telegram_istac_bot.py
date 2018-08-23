from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



token = open('token.txt').read()


def start(bot, update):
    id = update.message.from_user['id']
    bot.send_message(chat_id=id, text='¡Hola! Bienvenido al chatbot del ISTAC.')

def chatbot(bot, update):
    id = update.message.from_user['id']
    bot.send_message(chat_id=id, text='¡Hola! Bienvenido al chatbot del ISTAC.')


def main():

    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, start))

    print('ChatBot iniciado')
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('Iniciando ChatBot')
    main()