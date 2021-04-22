
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telebot
import pygame



print("Bot  WTP started")
bot = telebot.TeleBot('1777290579:AAGVarx5xRQ9QlPRx0L2LHyzgKMz-hDK284')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row( 'I Want to play', 'Free court','Statistic')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Welcome to Want To Play service. 
    We will help you to have those game that you want.
    Use the menu below. 
    Tape "Want To Play" to begin from start page.  '''
                     , reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Free court':
        bot.send_message(message.chat.id, 'At the moment we have the following free courts')

        #bot.send_photo(message.chat.id, open('E:\logo.jpg', 'rb'));
    elif message.text.lower() == 'продукты':
        bot.send_message(message.chat.id, 'Уникальные светильники уже в продаже.')
    elif message.text.lower() == 'акции':
        bot.send_message(message.chat.id, 'Акционные товары всегд апользуються спросом.')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


bot.polling()