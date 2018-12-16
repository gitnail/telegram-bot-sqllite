import os
import config
import sys
sys.path.append("../data_base")

from sqlite import SQLighter

DB_PATH = os.path.join("../data_base", config.database_name)


def do_safe(func, bot, message):
    try:
        func(message)
    except Exception as ex:
        bot.send_message(message.chat.id, "Error: '{}'".format(ex))


def execute(message, bot):
    def action(message):
        client = SQLighter(DB_PATH)
        res = client.execute(message.text)
        if not res:
            res = "<empty_reply>"
        bot.send_message(message.chat.id, str(res))

    do_safe(action, bot, message)


def get_by_date(message, bot):
    def action(message):
        date = datetime.datetime.strptime(message.text, "%Y-%M-%d")
        bot.send_message(message.chat.id, "Date format is correct")
    
    do_safe(action, bot, message)
