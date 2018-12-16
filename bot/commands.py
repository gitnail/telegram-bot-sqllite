import datetime
import tabletext

from wrappers import *


def execute(message, bot):
    def action(message, client):
        res = client.execute(message.text)
        send_result(bot, message, res)
        
    do_safe(action, bot, message)


def get_by_date(message, bot):
    def action(message, client):
        date = datetime.datetime.strptime(message.text, "%Y-%M-%d").date().isoformat()
        accidents = client.execute("""SELECT * FROM Accident WHERE SideConditionsID IN
                                (
                                    SELECT SideConditionsID FROM SideConditions WHERE DateTime = '{}'
                                )
                            """.format(date))

        res = []
        if accidents:
            res.append(["Index", "Date", "Sex", "Experience", "VehicleType"])
        cur_index = 0
        for accident in accidents:
            sex = client.execute("SELECT Sex FROM Participant WHERE ParticipantId = {}".format(accident[4]))[0][0]
            experience = client.execute("SELECT Experience FROM Participant WHERE ParticipantId = {}".format(accident[4]))[0][0]
            vechicle_type = client.execute("SELECT Type FROM Vechicle WHERE VechicleId = {}".format(accident[1]))[0][0]

            res.append([cur_index, date, sex, experience, vechicle_type])
            cur_index += 1
            
        send_result(bot, message, tabletext.to_text(res))

    do_safe(action, bot, message)
