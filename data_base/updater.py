from sqlite import *
from common import *

def add_accident(accident):
    sql = SQLighter("db_name.db")

    print(sql.execute("""
        CREATE TABLE Position (
            PositionID int,
            Latitude float,
            Longiture float
        );
        """))
    print(sql.execute("""
        CREATE TABLE Weather (
            WeatherID int,
            Light int,
            Wind int,
            Dumpness int
        );
        """))
    print(sql.execute("""
        CREATE TABLE SideConditions (
            SideConditionsID int,
            PositionID int,
            WeatherID int,
            DateTime varchar(255)
        );
        """))
    print(sql.execute("""
        CREATE TABLE Road (
            RoadID int,
            Type varchar(255),
            SpeedLimit int
        );
        """))
    print(sql.execute("""
        CREATE TABLE Police (
            PoliceID int,
            Rank varchar(255),
            District varchar(255)
        );
        """))
    print(sql.execute("""
        CREATE TABLE Vechicle (
            VechicleID int,
            Type varchar(255),
            Year varchar(255),
            Class varchar(255)
        );
        """))
    print(sql.execute("""
        CREATE TABLE Participant (
            ParticipantID int,
            HealthData varchar(255),
            Sex varchar(255),
            Age varchar(255),
            Experience int
        );
        """))
    print(sql.execute("""
        CREATE TABLE Accident (
            SideConditionsID int,
            VehicleID int,
            RoadID int,
            ParticipantID int,
            PoliceID int
        );
        """))
