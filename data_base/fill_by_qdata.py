import pandas
from create_data_base import *
from common import *
from updater import *

#create_data_base("accidents.db")

practice_data = pandas.read_csv('../qdata/Vehicles0515.csv')
practice_data.fillna(0)
print(practice_data.columns)

sql = SQLighter("accidents.db")

for index, row in practice_data[:50].iterrows():
    accident = Accident()

    accident.SideConditions.Position.Latitude = row["Latitude"]
    accident.SideConditions.Position.Longitude = row["Longitude"]
    accident.SideConditions.Weather.Light = row["Light"]
    accident.SideConditions.Weather.Wind = row["Wind"]

    accident.SideConditions.DateTime = row["Date"]

    add_accident(sql, accident)
