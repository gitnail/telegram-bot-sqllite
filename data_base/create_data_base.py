from sqlite import *

def create_data_base(name):
    sql = SQLighter(name)

    print(sql.execute("""
        CREATE TABLE SideConditions (
            SideConditionsID integer PRIMARY KEY AUTOINCREMENT,
            Weather integer,
            Date varchar(255),
            Latitude real,
            LightConditions integer,
            Longitude real
        );
        """))
    print(sql.execute("""
        CREATE TABLE Road (
            RoadID integer PRIMARY KEY AUTOINCREMENT,
            Type integer,
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
            Type integer,
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
            AccidentID integer PRIMARY KEY AUTOINCREMENT,
            SideConditionsID integer references SideConditions,
            VehicleID integer references Vehicle,
            RoadID integer references Road,
            ParticipantID integer references Participant,
            PoliceID integer references Police
        );
        """))

create_data_base("accidents.db")
