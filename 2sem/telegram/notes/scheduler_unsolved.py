import telebot
import init
from time_counter import Date
import re
from data_creater import Note

bot = "инициализировать бота"


@bot.message_handler(commands=['start'])
def start_bot(message):
    "написать приветсвие"


@bot.message_handler(commands=['addNotion'])
def add_notion(message):
    bot.send_message(message.chat.id, 'Введите дату в формате DD/MM/YY.')
    bot.register_next_step_handler(message, get_date)


def get_date(message):
    note = Note(int(message.text[:2]), int(message.text[3:5]), int(message.text[6:]))
    bot.send_message(message.chat.id, 'Введите дату в формате HH:MM-HH:MM.')
    bot.register_next_step_handler(message, get_time, note)


def get_time(message, note):
    time = message.text
    start_time = [int(time[:2]), int(time[3:5])]
    end_time = [int(time[-5:-3]), int(time[-2:])]

    note.add_time([start_time, end_time])
    bot.send_message(message.chat.id, 'Введите заметку.')
    bot.register_next_step_handler(message, get_text, note)


def get_text(message, note):
    note.create_note(message.text)


@bot.message_handler(commands=['allNotion'])
def all_notion(message):
    markup = "инициализировать клавиатуру"

    dates = Date()
    dates_array = dates.one_week()

    for date in dates_array:
        "добавить кнопки на клавиатуру"

    bot.send_message(message.chat.id, '............', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def drop_scheduler(message):
    match = re.fullmatch(r'\d\d.\d\d.\d\d', message.text)
    if match:
        bot.send_message(message.chat.id, '............')


if __name__ == '__main__':
    bot.infinity_polling()