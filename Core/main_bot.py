"""
Основа бота.
"""
import random
import telebot
from Poligon_1 import write_memory
from Other import tkn_bot as tkn

bot = telebot.TeleBot(tkn.API_TOKEN)

random_answer = ('Нет, не понимаю тебя...', 'Команда не распознана...')


@bot.message_handler(
    content_types=['text', 'document', 'audio'])  # Типы улавливания.
def get_text_messages(message):
    if message.text == "Раз":
        write_memory(message, 'w')
        bot.send_message(message.chat.id, "Два-два")
    elif message.text == "Два":
        bot.send_message(message.chat.id, "Три-три")
    else:
        bot.send_message(message.chat.id, random.choice(random_answer))


bot.polling(none_stop=True, interval=0)
