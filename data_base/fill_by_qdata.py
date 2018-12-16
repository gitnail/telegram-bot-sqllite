import pandas
#from create_data_base import *
from common import *
from updater import *

accident_data = pandas.read_csv('../qdata/Accidents0515.csv')
vehicles_data = pandas.read_csv('../qdata/Vehicles0515.csv')

sql = SQLighter("accidents.db")

for index, row in accident_data[:50].iterrows():
    accident = Accident()

    accident.SideConditions.Latitude = row["Latitude"]
    accident.SideConditions.Longitude = row["Longitude"]
    accident.SideConditions.DateTime = row["Date"]

    add_accident(sql, accident)
