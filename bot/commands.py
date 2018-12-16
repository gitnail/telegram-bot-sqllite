import datetime

from wrappers import *

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
