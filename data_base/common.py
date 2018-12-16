from random import randint

class Position
    def __init__(self):
        self.PositionID = randint(0, 100000)
        self.Latitude= 0.0
        self.Longiture= 0.0

class Weather
    def __init__(self):
        self.WeatherID = randint(0, 100000)
        self.Light = randint(0, 100000)
        self.Wind = randint(0, 100000)
        self.Dumpness = randint(0, 100000)

class SideConditions
    def __init__(self):
        self.SideConditionsID = randint(0, 100000)
        self.PositionID = randint(0, 100000)
        self.WeatherID = randint(0, 100000)
        self.DateTime varchar(255)

class Road 
    def __init__(self):
        self.RoadID = randint(0, 100000)
        self.Type = "normal"
        self.SpeedLimit = 60

class Police
    def __init__(self):
        self.PoliceID = randint(0, 100000)
        self.Rank = "officer"
        self.District = "leninsky"

class Vechicle 
        def __init__(self):
        self.VechicleID = randint(0, 100000)
        self.Type = "Machine"
        self.Year = 1998
        self.Class = "S"

class Participant 
    def __init__(self):
        self.ParticipantID = randint(0, 100000)
        self.HealthData = "healthy"
        self.Sex = "male"
        self.Age = 20
        self.Experience = 5

class Accident 
    def __init__(self):
        self.SideConditionsID = randint(0, 100000)
        self.VehicleID = randint(0, 100000)
        self.RoadID = randint(0, 100000)
        self.ParticipantID = randint(0, 100000)
        self.PoliceID = randint(0, 100000)
