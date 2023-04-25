import telebot
import init

bot = telebot.TeleBot(init.TOKEN)

@bot.message_handler(commands=['start'])
def greetings(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    image = telebot.types.KeyboardButton("dropImage")
    video = telebot.types.KeyboardButton("dropVideo")
    joke = telebot.types.KeyboardButton("dropJoke")

    markup.add(image)
    markup.add(video)
    markup.add(joke)

    bot.send_message(message.chat.id, 'Бот кидающий рандомные мемы.\n'
                                      'Список команд :\n'
                                      'dropImage - присылает случайную картинку.\n'
                                      'dropVideo - присылает случайное видео с Youtube.\n'
                                      'dropJoke - присылает случайную шутку.',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def drop_memes(message):
    if message.text == "dropImage":
        img = open("mem1.jpg", 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text == "dropVideo":
        bot.send_message(message.chat.id, '2')
    elif message.text == "dropJoke":
        bot.send_message(message.chat.id, '3')

if __name__ == "__main__":
    bot.infinity_polling()