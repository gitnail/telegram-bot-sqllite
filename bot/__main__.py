#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from telebot import types

from commands import *

BOT = telebot.TeleBot(config.token)
 
WORKER = {}


@BOT.message_handler(commands=["start"])
def handle_start(message):
    BOT.send_message(message.chat.id, "Welcome to accidents DB client using SQLite DB")


@BOT.message_handler(commands=["help"])
def handle_help(message):
    BOT.send_message(message.chat.id, "TODO")


@BOT.message_handler(commands=["get_by_date"])
def handle_get_by_date(message):
    markup = types.ForceReply(selective=False)
    WORKER.update({message.from_user.id: get_by_date})
    BOT.send_message(message.chat.id, "Please enter a date", reply_markup=markup)


@BOT.message_handler(commands=["execute"])
def handle_execute(message):
    markup = types.ForceReply(selective=False)
    WORKER.update({message.from_user.id: execute})
    BOT.send_message(message.chat.id, "Please enter an SQL command to execute", reply_markup=markup)


@BOT.message_handler(content_types=["text"])
def handle_text(message):
    uid = message.from_user.id
    if uid in WORKER:
        WORKER[uid](message, BOT)
        try:
            del WORKER[uid]
        except:
            pass
    else:
        BOT.send_message(message.chat.id, "Id dont' undestand :(")


if __name__ == "__main__":
    BOT.polling(none_stop=True)
