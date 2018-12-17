import config
import os
import sys
sys.path.append("../data_base")

from sqlite import SQLighter

DB_PATH = os.path.join("../data_base", config.database_name)


def do_safe(func, bot, message):
    try:
        client = SQLighter(DB_PATH)
        func(message, client)
    except Exception as ex:
        bot.send_message(message.chat.id, "Error: '{}'".format(ex))
        raise ex


def send_result(bot, message, res):
    if not res:
        res = "<empty_reply>"
    bot.send_message(message.chat.id, "```{}```".format(res), parse_mode="Markdown")

