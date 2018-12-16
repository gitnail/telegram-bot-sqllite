from random import randint

class SideConditions:
    def __init__(self):
        self.Weather = randint(0, 10000)
        self.Light = 0
        self.Latitude= 0.0
        self.Longitude= 0.0
        self.DateTime = "2018-01-01"

class Road:
    def __init__(self):
        self.Type = 0
        self.SpeedLimit = 60

class Police:
    def __init__(self):
        self.Rank = "officer"
        self.District = "leninsky"

class Vechicle:
    def __init__(self):
        self.Type = "Machine"
        self.Year = 1998
        self.Class = "S"

class Participant:
    def __init__(self):
        self.HealthData = "healthy"
        self.Sex = "male"
        self.Age = 20
        self.Experience = 5

class Accident:
    def __init__(self):
        self.SideConditions = SideConditions()
        self.Vehicle = Vechicle()
        self.Road = Road()
        self.Participant = Participant()
        self.Police = Police()
        self.ExternalID = ""
