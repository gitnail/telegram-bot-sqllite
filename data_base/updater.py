from sqlite import *
from common import *

def add_side_conditions(sql, side_conditions):
    sql.execute('INSERT INTO SideConditions (Weather, Date, Latitude, Longitude, LightConditions) values (%s, "%s", %s, %s, %s);'
        % (side_conditions.Weather, side_conditions.DateTime.replace('/', '-'), side_conditions.Latitude, side_conditions.Longitude, side_conditions.Light))
    side_conditions_id = sql.last_insert_rowid()
    print("add_side_conditions id:", side_conditions_id)
    return side_conditions_id

def add_road(sql, road):
    sql.execute('INSERT INTO Road (Type, SpeedLimit) values (%s, %s);' % (road.Type, road.SpeedLimit))
    road_id = sql.last_insert_rowid()
    print("add_road id:", road_id)
    return road_id

def add_police(sql, police):
    sql.execute('INSERT INTO Police (Rank, District) values ("%s", "%s");' % (police.Rank, police.District))
    police_id = sql.last_insert_rowid()
    print("add_police id:", police_id)
    return police_id

def add_vehicle(sql, vehicle):
    sql.execute('INSERT INTO Vehicle (Type, Year, Class) values (%s, %s, "%s");' % (vehicle.Type, vehicle.Year, vehicle.Class))
    vehicle_id = sql.last_insert_rowid()
    print("add_vehicle id:", vehicle_id)
    return vehicle_id

def add_participant(sql, participant):
    sql.execute('INSERT INTO Participant (HealthData, Sex, Age, Experience) values ("%s", "%s", %s, %s);'
        % (participant.HealthData, participant.Sex, participant.Age, participant.Experience))
    participant_id = sql.last_insert_rowid()
    print("add_participant id:", participant_id)
    return participant_id

def add_accident(sql, accident):
    side_conditions_id = add_side_conditions(sql, accident.SideConditions)
    road_id = add_road(sql, accident.Road)
    police_id = add_police(sql, accident.Police)
    vehicle_id = add_vehicle(sql, accident.Vehicle)
    participant_id = add_participant(sql, accident.Participant)
    print(sql.execute('INSERT INTO Accident (SideConditionsID, VehicleID, RoadID, ParticipantID, PoliceID, ExternalID) values (%s, %s, %s, %s, %s, "%s");'
        % (
            side_conditions_id,
            vehicle_id,
            road_id,
            participant_id,
            police_id,
            accident.ExternalID
        )))
    accident_id = sql.last_insert_rowid()
    print("added accident:", accident_id)
    return accident_id

