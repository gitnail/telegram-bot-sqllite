#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import datetime
import sys
import telebot
from telebot import types

sys.path.append("../data_base")

from client import SQLClient


bot = telebot.TeleBot(config.token)

#clent = SQLClinet(config.database_name)

def get_by_date(message):
    try:
        date = datetime.datetime.strptime(message.text, "%Y-%M-%d")
        bot.send_message(message.chat.id, "Date's format is correct")
    except Exception as ex:
        bot.send_message(message.chat.id, "Error: {}".format(ex))

worker = {}

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to accidents DB client using SQLite DB")

@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, "TODO")

@bot.message_handler(commands=["get_by_date"])
def handle_get_by_date(message):
    markup = types.ForceReply(selective=False)
    worker.update({message.from_user.id: get_by_date})
    bot.send_message(message.chat.id, "Please enter a date", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    uid = message.from_user.id
    if uid in worker:
        worker[uid](message)
    else:
        bot.send_message(message.chat.id, "Id dont' undestand :(")


if __name__ == "__main__":
    bot.polling(none_stop=True)
