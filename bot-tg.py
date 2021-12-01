from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import security

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot-tg.log'
                    )

def greet_user(update, bot):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(update, bot):
    user_text = update.message.text
    print(user_text)
    up_mess = update.message
    logging.info("Привет {}, ты написал {}, твой id {}".format(up_mess.chat.first_name, up_mess.text, up_mess.chat.id))
    update.message.reply_text(user_text)

def main():
        mybot = Updater(security.API_KEY)
        logging.info('Бот запускается')
        dp = mybot.dispatcher
        dp.add_handler(CommandHandler('start', greet_user))
        dp.add_handler(MessageHandler(Filters.text, talk_to_me))

        mybot.start_polling()
        mybot.idle()

main()
