import telebot
from telebot import types
from select_db import get_db

bot = telebot.TeleBot('6083360054:AAF4bHUzjdkWyXNxWTFmTmMCDOx1l0ipY2M')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('от 1000')
        btn2 = types.KeyboardButton('от 1000')
        btn3 = types.KeyboardButton('от 2000')
        btn4 = types.KeyboardButton('от 3000')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Выберете сложность задания', reply_markup=markup) # ответ бота

    elif message.text == 'от 0':
        db = get_db(0)
        for i in range(10):
            bot.send_message(message.from_user.id, f"{db[i]}", parse_mode='Markdown')

    elif message.text == 'от 1000':
        db = get_db(1000)
        for i in range(10):
            bot.send_message(message.from_user.id, f"{db[i]}", parse_mode='Markdown')

    elif message.text == 'от 2000':
        db = get_db(2000)
        for i in range(10):
            bot.send_message(message.from_user.id, f"{db[i]}", parse_mode='Markdown')

    elif message.text == 'от 3000':
        db = get_db(3000)
        for i in range(10):
            bot.send_message(message.from_user.id, f"{db[i]}", parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

