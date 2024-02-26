
from telebot import types
import telebot

API_TOKEN = '5928296158:AAETw4a7bVe_L4FUGmELqmYceFTe3uPJ7pI'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я ваш телеграм-бот!")

# Этот код отправит обратно все текстовые сообщения, которые получит бот.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

# Этот код обработает фотографии, отправленные пользователем, и отправит ответное сообщение.
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Обработка фотографии
    bot.send_message(message.chat.id, "Спасибо за изображение!")

# Этот код создает и отправляет клавиатуру при вызове команды /keyboard.


@bot.message_handler(commands=['keyboard'])
def handle_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Нажми меня")
    markup.add(item)

    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

# Этот код обрабатывает нажатие кнопки "Нажми меня" в клавиатуре.
@bot.message_handler(func=lambda message: message.text == "Нажми меня")
def handle_key(message):
    bot.send_message(message.chat.id, "Вы нажали на кнопку!")

bot.polling()