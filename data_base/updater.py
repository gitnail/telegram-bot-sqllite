from sqlite import *
from common import *

def add_accident(accident):
    sql = SQLighter("accidents.db")

    position = accident.SideConditions.Position
    print(sql.execute('INSERT INTO Position (Latitude, Longitude) values (%s, %s);' % (position.Latitude, position.Longitude)))
    position_id = sql.last_insert_rowid()

    weather = accident.SideConditions.Weather
    print(sql.execute('INSERT INTO Weather (Light, Wind, Dumpness) values (%s, %s, %s);'
        % (weather.Light, weather.Wind, weather.Dumpness)))
    weather_id = sql.last_insert_rowid()

    side_conditions = accident.SideConditions
    print(sql.execute('INSERT INTO SideConditions (PositionID, WeatherID, DateTime) values (%s, %s, "%s");'
        % (position_id, weather_id, side_conditions.DateTime)))
    side_conditions_id = sql.last_insert_rowid()

    road = accident.Road
    print(sql.execute('INSERT INTO Road (Type, SpeedLimit) values ("%s", %s);'
        % (road.Type, road.SpeedLimit)))
    road_id = sql.last_insert_rowid()

    police = accident.Police
    print(sql.execute('INSERT INTO Police (Rank, District) values ("%s", "%s");'
        % (police.Rank, police.District)))
    police_id = sql.last_insert_rowid()

    vehicle = accident.Vehicle
    print(sql.execute('INSERT INTO Vehicle (Type, Year, Class) values ("%s", %s, "%s");'
        % (vehicle.Type, vehicle.Year, vehicle.Class)))
    vehicle_id = sql.last_insert_rowid()

    participant = accident.Participant
    print(sql.execute('INSERT INTO Participant (HealthData, Sex, Age, Experience) values ("%s", "%s", %s, %s);'
        % (participant.HealthData, participant.Sex, participant.Age, participant.Experience)))
    participant_id = sql.last_insert_rowid()

    print(sql.execute('INSERT INTO Accident (SideConditionsID, VehicleID, RoadID, ParticipantID, PoliceID) values (%s, %s, %s, %s, %s);'
        % (
            side_conditions_id,
            vehicle_id,
            road_id,
            participant_id,
            police_id
        )))
    accident_id = sql.last_insert_rowid()
    print("added accident:", accident_id)


accident = Accident()

add_accident(accident)
