import pandas
#from create_data_base import *
from common import *
from updater import *

accident_data = pandas.read_csv('../qdata/Accidents0515.csv')
vehicles_data = pandas.read_csv('../qdata/Vehicles0515.csv')

sql = SQLighter("accidents.db")

accidents = []

for index, row in accident_data[:3500].iterrows():
    accident = Accident()

    accident.SideConditions.Latitude = row["Latitude"]
    accident.SideConditions.Longitude = row["Longitude"]
    accident.SideConditions.DateTime = row["Date"]
    accident.SideConditions.Light = row["Light_Conditions"]
    accident.SideConditions.Weather = row["Weather_Conditions"]

    accident.Road.Type = row["Road_Type"]
    accident.Road.SpeedLimit = row["Speed_limit"]

    accident.ExternalID = row["Accident_Index"]

    accidents.append(accident)

for index, row in vehicles_data[:3500].iterrows():
    accident = accidents[index]
    
    accident.Vehicle.Type = row["Vehicle_Type"]

    accident.Participant.Sex = row["Sex_of_Driver"]
    accident.Participant.Age = row["Age_of_Driver"]
    accident.Participant.Experience = row["Driving_Experience"]


    add_accident(sql, accident)
