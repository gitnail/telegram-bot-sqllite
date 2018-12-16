import config
import datetime
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


def send_result(bot, message, res):
    if not res:
        res = "<empty_reply>"
    bot.send_message(message.chat.id, str(res))


def execute(message, bot):
    def action(message, client):
        res = client.execute(message.text)
        send_result(bot, message, res)
        
    do_safe(action, bot, message)


def get_by_date(message, bot):
    def action(message, client):
        date = datetime.datetime.strptime(message.text, "%Y-%M-%d").date().isoformat()
        res = client.execute("""SELECT * FROM Accident WHERE SideConditionsID IN
                                (
                                    SELECT SideConditionsID FROM SideConditions WHERE DateTime = '{date}'
                                )
                            """.format(date = date))
        send_result(bot, message, res)

    do_safe(action, bot, message)
