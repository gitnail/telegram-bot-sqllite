def id_to_string_road_type(id):
    if id == 1:
        return "Roundabout"
    if id == 2:
        return "One way street"
    if id == 3:
        return "Dual carriageway"
    if id == 6:
        return "Single carriageway"
    if id == 7:
        return "Slip road"
    if id == 9:
        return "Unknown"
    if id == 2:
        return "One way street/Slip road"
    if id == -1:
        return "Data missing or out of range"
    return ""

def id_to_string_light_conditions(id):
    if id == 1:
        return "Daylight"
    if id == 4:
        return "Darkness - lights lit"
    if id == 5:
        return "Darkness - lights unlit"
    if id == 6:
        return "Darkness - no lighting"
    if id == 7:
        return "Darkness - lighting unknown"
    if id == -1:
        return "Data missing or out of range"
    return ""

def id_to_string_weather(id):
    if id == 1:
        return "Fine no high winds"
    if id == 2:
        return "Raining no high winds"
    if id == 3:
        return "Snowing no high winds"
    if id == 4:
        return "Fine + high winds"
    if id == 5:
        return "Raining + high winds"
    if id == 6:
        return "Snowing + high winds"
    if id == 7:
        return "Fog or mist"
    if id == 8:
        return "Other"
    if id == 9:
        return "Unknown"
    if id == -1:
        return "Data missing or out of range"
    return ""

def id_to_string_vehicle_type(id):
    if id == 1:
        return "Pedal cycle"
    if id == 2:
        return "Motorcycle 50cc and under"
    if id == 3:
        return "Motorcycle 125cc and under"
    if id == 4:
        return "Motorcycle over 125cc and up to 500cc"
    if id == 5:
        return "Motorcycle over 500cc"
    if id == 8:
        return "Taxi/Private hire car"
    if id == 9:
        return "Car"
    if id == 10:
        return "Minibus (8 - 16 passenger seats)"
    if id == 11:
        return "Bus or coach (17 or more pass seats)"
    if id == 16:
        return "Ridden horse"
    if id == 17:
        return "Agricultural vehicle"
    if id == 18:
        return "Tram"
    if id == 19:
        return "Van / Goods 3.5 tonnes mgw or under"
    if id == 20:
        return "Goods over 3.5t. and under 7.5t"
    if id == 21:
        return "Goods 7.5 tonnes mgw and over"
    if id == 22:
        return "Mobility scooter"
    if id == 23:
        return "Electric motorcycle"
    if id == 90:
        return "Other vehicle"
    if id == 97:
        return "Motorcycle - unknown cc"
    if id == 98:
        return "Goods vehicle - unknown weight"
    if id ==-1:
        return "Data missing or out of range"
    return ""

def id_to_string_sex(id):
    if id == 1:
        return "Male"
    if id == 2:
        return "Female"
    if id == 3:
        return "Not known"
    if id == -1:
        return "Data missing or out of range"
    return ""
