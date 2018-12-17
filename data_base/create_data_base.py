from sqlite import *

def create_data_base(name):
    sql = SQLighter(name)

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
        CREATE TABLE IF NOT EXISTS Accident (
            AccidentID integer PRIMARY KEY AUTOINCREMENT,
            RoadID integer references Road,
            PoliceID integer references Police,
            ExternalID varchar(255)
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS Vechicle (
            VechicleID integer PRIMARY KEY AUTOINCREMENT,
            AccidentID integer references Accident,
            Type integer,
            Year varchar(255),
            Class varchar(255)
        );
        """)
    sql.execute("""
        CREATE TABLE IF NOT EXISTS SideConditions (
            SideConditionsID integer PRIMARY KEY AUTOINCREMENT,
            AccidentID integer references Accident,
            Weather integer,
            Date varchar(255),
            Latitude real,
            LightConditions integer,
            Longitude real
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
        CREATE TABLE IF NOT EXISTS Participate (
            AccidentID integer Accident,
            ParticipantID integer references Participant,
            primary key (AccidentID, ParticipantID)
        );
        """)
    print("all tables created")

create_data_base("accidents.db")
