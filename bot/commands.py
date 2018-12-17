import datetime
import sys
import tabletext
sys.path.append("../helpers")

from id_to_string import *
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
        accidents = client.execute("""SELECT SideConditions.Date, Participant.Sex, Participant.Experience, Vechicle.Type FROM
                                    SideConditions JOIN Participate ON (SideConditions.AccidentId=Participate.AccidentId) JOIN Participant ON
                                    (Participate.ParticipantID=Participant.ParticipantID) JOIN Vechicle ON (Vechicle.AccidentId=Participate.AccidentId)
                                    WHERE SideConditions.Date = '{}'
                                    """.format(date))

        print(accidents)

        res = []
        if accidents:
            res.append(["Date", "Sex", "Experience", "VechicleType"])
        for accident in accidents:
            res.append([accident[0], id_to_string_sex(to_int(accident[1])), str(accident[2]), id_to_string_vehicle_type(to_int(accident[3]))])
        
        text = make_table(res)
        if accidents:
            cnt = client.execute("SELECT COUNT(DISTINCT AccidentId) FROM SideConditions WHERE Date = '{}'".format(date))[0][0]
            bot.send_message(message.chat.id, "Total accidents count: {}".format(cnt))
        send_result(bot, message, text)

    do_safe(action, bot, message)

def to_int(obj):
    if not obj:
        return -1
    return int(obj)

def group_by_weather(message, bot):
    def action(message, client):
        selected = client.execute("""SELECT Weather, Count(Weather) AS Count
                                        FROM
                                            (
                                                SELECT DISTINCT SideConditionsId, Weather
                                                FROM SideConditions
                                            )
                                        GROUP BY Weather
                                  """)
        
        res = []
        if selected:
            res.append(["Weather", "Count"])
        for it in selected:
            res.append([id_to_string_weather(to_int(it[0])), str(it[1])])
            
        send_result(bot, message, make_table(res))

        print(selected)

    do_safe(action, bot, message)


def darkness_mean_experience(message, bot):
    def action(message, client):
        res = client.execute("""SELECT AVG(Participant.Experience) FROM SideConditions JOIN Participate ON
                                    (SideConditions.AccidentId=Participate.AccidentId) JOIN Participant ON (Participate.ParticipantID=Participant.ParticipantID)
                                    WHERE SideConditions.LightConditions > 1 AND Participant.Sex = {} AND Participant.Experience <> -1
                                """.format(message.text))[0][0]
        send_result(bot, message, res)

    do_safe(action, bot, message)


def count_by_vehicle_type(message, bot):
    def action(message, client):
        selected = client.execute("""SELECT Police.District, COUNT(DISTINCT Accident.AccidentID) FROM Police JOIN Accident ON
                                    (Police.PoliceID=Accident.PoliceID) JOIN Vechicle ON (Accident.AccidentID=Vechicle.AccidentID)
                                    WHERE Vechicle.Type={}
                                    GROUP BY Police.District
                                """.format(message.text))
        print(selected)
        res = []
        if selected:
            res.append(["District", "Count"])
        for it in selected:
            res.append([it[0], str(it[1])])
        
        send_result(bot, message, make_table(res))


    do_safe(action, bot, message)


def max_speed_limit(message, bot):
    def action(message, client):
        res = client.execute("""SELECT MAX(Road.SpeedLimit) FROM Road JOIN Accident ON
                                (Road.RoadID=Accident.RoadID) JOIN Participate ON
                                (Accident.AccidentID=Participate.AccidentID) JOIN Participant ON
                                (Participate.ParticipantID=Participant.ParticipantID)
                                WHERE CAST(Participant.Age AS SIGNED) < {}
                                """.format(message.text))[0][0]
        send_result(bot, message, res)

    do_safe(action, bot, message)


def remove_side_conditions(message, bot):
    def action(message, client):
        date = datetime.datetime.strptime(message.text, "%d-%M-%Y").date().strftime("%d-%m-%Y")
        client.execute("DELETE FROM SideConditions WHERE Date = '{}'".format(date))
        send_result(bot, message, "Side conditions by {} successfully removed from data base".format(date))

    do_safe(action, bot, message)

def add_accident(message, bot):
    def action(message, client):
        fields = message.text.split(",")
        for i in range(len(fields)):
            fields[i] = fields[i].strip()

        date = datetime.datetime.strptime(fields[0], "%d-%M-%Y").date().strftime("%d-%m-%Y")  # validate date

        client.execute("INSERT INTO Accident (RoadID, PoliceID, ExternalID) values (NULL, NULL, NULL);")
        accident_id = client.last_insert_rowid()
        client.execute("INSERT INTO SideConditions (Weather, Date, Latitude, Longitude, LightConditions, AccidentID) values (NULL, '{}', NULL, NULL, NULL, {});".format(date, accident_id))
        client.execute("INSERT INTO Participant (HealthData, Sex, Age, Experience) values (NULL, {}, NULL, NULL);".format(fields[1]))
        participant_id = client.last_insert_rowid()
        client.execute("INSERT INTO Participate (AccidentID, ParticipantID) values ({}, {});".format(accident_id, participant_id))
        client.execute("INSERT INTO Vechicle (Type, Year, Class, AccidentID) values ({}, NULL, NULL, {});".format(fields[2], accident_id))
        send_result(bot, message, "Accident added to data base")

    do_safe(action, bot, message)
