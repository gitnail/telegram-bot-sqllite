from random import randint

class Position:
    def __init__(self):
        self.Latitude= 0.0
        self.Longitude= 0.0

class Weather:
    def __init__(self):
        self.Light = randint(0, 100000)
        self.Wind = randint(0, 100000)
        self.Dumpness = randint(0, 100000)

class SideConditions:
    def __init__(self):
        self.Position = Position()
        self.Weather = Weather()
        self.DateTime = "2018-01-01"

class Road:
    def __init__(self):
        self.Type = "normal"
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
