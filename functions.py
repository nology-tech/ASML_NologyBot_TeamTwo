import math

def find_legs(directions):
    number_of_legs = len(directions[0]["legs"])
    return number_of_legs

def find_distance(directions):
    distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
    return f"{distance} mi"

def find_time(directions):
    time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
    return f"{time} hrs"

def find_speed(directions):
    distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
    time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
    speed = math.floor(distance/time)
    return f"{speed} mph"

def find_startLatLon(directions):
    startLatLon = directions[0]["legs"][0]["start_location"]
    return startLatLon

def find_endLatLon(directions):
    endLatLon = directions[0]["legs"][0]["end_location"]
    return endLatLon

def find_travelModes(directions):
    travelModes = []
    for mode in directions[0]["legs"][0]["steps"]:
        travelModes.append(mode["travel_mode"].lower())
    travelList = []
    for word in travelModes:
        if word not in travelList:
            travelList.append(word)
    return travelList
  
def create_summary(directions, origin, destination):
    distance = find_distance(directions)
    time = find_time(directions)
    speed = find_speed(directions)
    travelList = find_travelModes(directions)
    travelList2 = []
    for word in travelList:
        if word == "transit":
            word = "taking public " + word
            travelList2.append(word)
        else:
            travelList2.append(word)
    travelSentence = "/".join(travelList2)
    summary = f"You will be starting at {origin} and {travelSentence} a total distance of {distance} with an average speed of {speed} until you reach your destination at {destination}."
    return summary