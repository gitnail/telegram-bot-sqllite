from sqlite import *

def create_data_base(name):
    sql = SQLighter(name)

    print(sql.execute("""
        CREATE TABLE Position (
            PositionID integer PRIMARY KEY AUTOINCREMENT,
            Latitude real,
            Longitude real
        );
        """))
    print(sql.execute("""
        CREATE TABLE Weather (
            WeatherID integer PRIMARY KEY AUTOINCREMENT,
            Light int,
            Wind int,
            Dumpness int
        );
        """))
    print(sql.execute("""
        CREATE TABLE SideConditions (
            SideConditionsID integer PRIMARY KEY AUTOINCREMENT,
            PositionID integer,
            WeatherID integer,
            DateTime varchar(255)
        );
        """))
    print(sql.execute("""
        CREATE TABLE Road (
            RoadID integer PRIMARY KEY AUTOINCREMENT,
            Type varchar(255),
            SpeedLimit int
        );
        """))
    print(sql.execute("""
        CREATE TABLE Police (
            PoliceID integer PRIMARY KEY AUTOINCREMENT,
            Rank varchar(255),
            District varchar(255)
        );
        """))
    print(sql.execute("""
        CREATE TABLE Vehicle (
            VechicleID integer PRIMARY KEY AUTOINCREMENT,
            Type varchar(255),
            Year varchar(255),
            Class varchar(255)
        );
        """))
    print(sql.execute("""
        CREATE TABLE Participant (
            ParticipantID integer PRIMARY KEY AUTOINCREMENT,
            HealthData varchar(255),
            Sex varchar(255),
            Age varchar(255),
            Experience int
        );
        """))
    print(sql.execute("""
        CREATE TABLE Accident (
            SideConditionsID integer PRIMARY KEY AUTOINCREMENT,
            VehicleID integer,
            RoadID integer,
            ParticipantID integer,
            PoliceID int
        );
        """))
