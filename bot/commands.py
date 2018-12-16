import datetime
import tabletext

from wrappers import *


def execute(message, bot):
    def action(message, client):
        res = client.execute(message.text)
        send_result(bot, message, res)
        
    do_safe(action, bot, message)

def make_table(array):
    try:
        return tabletext.to_text(array)
    except:
        return ""

def get_by_date(message, bot):
    def action(message, client):
        date = datetime.datetime.strptime(message.text, "%d-%M-%Y").date().strftime("%d-%m-%Y")
        print(date)
        accidents = client.execute("""SELECT * FROM Accident WHERE SideConditionsID IN
                                (
                                    SELECT SideConditionsID FROM SideConditions WHERE Date = '{}'
                                )
                            """.format(date))

        res = []
        if accidents:
            res.append(["Accident Id", "Date", "Sex", "Experience", "VechicleType"])
        for accident in accidents:
            sex = client.execute("SELECT Sex FROM Participant WHERE ParticipantId = {}".format(accident[4]))[0][0]
            experience = client.execute("SELECT Experience FROM Participant WHERE ParticipantId = {}".format(accident[4]))[0][0]
            vechicle_type = client.execute("SELECT Type FROM Vechicle WHERE VechicleId = {}".format(accident[2]))[0][0]

            res.append([accident[0], date, sex, experience, vechicle_type])
            
        send_result(bot, message, make_table(res))

    do_safe(action, bot, message)
