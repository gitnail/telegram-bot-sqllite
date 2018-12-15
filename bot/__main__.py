#! /usr/bin/env python3
import config
import sys
import telebot


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to accidents DB client")

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, "TODO")

if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            print(ex, file=sys.stderr)
