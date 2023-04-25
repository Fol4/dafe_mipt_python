import telebot
import init

bot = telebot.TeleBot(init.TOKEN)

@bot.message_handler(content_types=['text'])
def resend_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.infinity_polling()