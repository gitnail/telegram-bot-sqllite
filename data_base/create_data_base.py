from sqlite import *

def create_data_base(name):
    sql = SQLighter(name)

    sql.execute("""
        CREATE TABLE IF NOT EXISTS SideConditions (
            SideConditionsID integer PRIMARY KEY AUTOINCREMENT,
            Weather integer,
            Date varchar(255),
            Latitude real,
            LightConditions integer,
            Longitude real
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS Road (
            RoadID integer PRIMARY KEY AUTOINCREMENT,
            Type integer,
            SpeedLimit int
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS Police (
            PoliceID integer PRIMARY KEY AUTOINCREMENT,
            Rank varchar(255),
            District varchar(255)
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS Vechicle (
            VechicleID integer PRIMARY KEY AUTOINCREMENT,
            Type integer,
            Year varchar(255),
            Class varchar(255)
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS Participant (
            ParticipantID integer PRIMARY KEY AUTOINCREMENT,
            HealthData varchar(255),
            Sex varchar(255),
            Age varchar(255),
            Experience int
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS Accident (
            AccidentID integer PRIMARY KEY AUTOINCREMENT,
            SideConditionsID integer references SideConditions,
            VechicleID integer references Vechicle,
            RoadID integer references Road,
            ParticipantID integer references Participant,
            PoliceID integer references Police
        );
        """)
    print("all tables created")

create_data_base("accidents.db")
