#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
import time
from telebot import types
import sys
sys.path.append("../helpers")

from commands import *
from id_to_string import *

from telebot import apihelper

BOT = telebot.TeleBot(config.token)
 
WORKER = {}


@BOT.message_handler(commands=["start"])
def handle_start(message):
    BOT.send_message(message.chat.id, "Welcome to accidents DB client using SQLite DB")

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


@BOT.message_handler(commands=["group_by_weather"])
def handle_group_by_weather(message):
    group_by_weather(message, BOT)


@BOT.message_handler(commands=["count_by_vehicle_type"])
def handle_count_by_vehicle_type(message):
    markup = types.ForceReply(selective=False)
    names = ["Vehicle type keys:"]
    for i in range(-1, 201):
        name = id_to_string_vehicle_type(i)
        if name:
            names.append("{}: {}".format(i, name))
    BOT.send_message(message.chat.id, "\n".join(names))
    WORKER.update({message.from_user.id: count_by_vehicle_type})
    BOT.send_message(message.chat.id, "Please enter a vehicle type", reply_markup=markup)


@BOT.message_handler(commands=["darkness_mean_experience"])
def handle_darkness_mean_experience(message):
    markup = types.ForceReply(selective=False)
    names = ["Sex keys:"]  # 18+
    for i in range(-1, 4):
        name = id_to_string_sex(i)
        if name:
            names.append("{}: {}".format(i, name))
    BOT.send_message(message.chat.id, "\n".join(names))

    WORKER.update({message.from_user.id: darkness_mean_experience})
    BOT.send_message(message.chat.id, "Please enter a sex of driver", reply_markup=markup)


@BOT.message_handler(commands=["max_speed_limit"])
def handle_max_speed_limit(message):
    markup = types.ForceReply(selective=False)
    WORKER.update({message.from_user.id: max_speed_limit})
    BOT.send_message(message.chat.id, "Please enter an age of driver", reply_markup=markup)


@BOT.message_handler(commands=["remove_side_conditions"])
def handle_remove_side_conditions(message):
    markup = types.ForceReply(selective=False)
    WORKER.update({message.from_user.id: remove_side_conditions})
    BOT.send_message(message.chat.id, "Please enter a date", reply_markup=markup)


@BOT.message_handler(commands=["add_accident"])
def handle_add_accident(message):
    markup = types.ForceReply(selective=False)
    WORKER.update({message.from_user.id: add_accident})
    BOT.send_message(message.chat.id, "Enter accident in format: '<Date>,<Sex>,<Vehicle_Type>'", reply_markup=markup)



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
        BOT.send_message(message.chat.id, "I dont' understand :(")


if __name__ == "__main__":
    while True:
        try:
            BOT.polling(none_stop=True)
        except:
            time.sleep(2)
