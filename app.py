from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import googlemaps
import json
import math


def create_app(config):
    load_dotenv() 
    api_key = os.getenv("API_KEY") 
    app = Flask(__name__)
    

    gmaps = googlemaps.Client(api_key)

    @app.get("/")
    def home():
        return render_template("homepage.html")

    @app.route("/directions/<x>/<y>/<z>", methods=["GET"])
    def get_directions(x, y, z):
        directions_result = gmaps.directions(origin = x, destination = y, mode = z)
        if directions_result:
            return json.dumps({"distance": find_distance(directions_result),
                                "time": find_time(directions_result),
                                "speed": find_speed(directions_result),
                                "startLatLon": find_startLatLon(directions_result),
                                "endLatLon": find_endLatLon(directions_result),
                                "travelModes": find_travelModes(directions_result),
                                "summary": create_summary(directions_result, x, y)}, indent=4), 200
        else:
            return json.dumps({"error": "An error occurred or there are no available directions for this search."}), 404

    def find_distance(directions):
        distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
        return distance

    def find_time(directions):
        time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
        return time

    def find_speed(directions):
        distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
        time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
        speed = math.floor(distance/time)
        return speed

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
        distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
        time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
        speed = math.floor(distance/time)
        endLatLon = directions[0]["legs"][0]["end_location"]
        startLatLon = directions[0]["legs"][0]["start_location"]
        travelModes = []
        for mode in directions[0]["legs"][0]["steps"]:
            travelModes.append(mode["travel_mode"].lower())
        travelList = []
        for word in travelModes:
            if word not in travelList:
                travelList.append(word)
        travelList2 = []
        for word in travelList:
            if word == "transit":
                word = "taking public " + word
                travelList2.append(word)
            else:
                travelList2.append(word)
        travelSentence = "/".join(travelList2)
        summary = f"You will be starting at {origin} and {travelSentence} a total distance of {distance} miles with an average speed of {speed} mph until you reach your destination at {destination}."

        return json.dumps({"number of legs": len(directions[0]["legs"]),
                            "distance traveled": f"{distance} mi",
                            "travel time": f"{time} hrs",
                            "average speed": f"{speed} mph",
                            "startLatLon": startLatLon,
                            "endLatLon": endLatLon,
                            "travel mode": travelList,
                            "summary of trip": summary
        }, indent=4)

    return app

app = create_app({"TESTING": False})

if __name__ == "__main__":  #pragma: no cover
    app.run(DEBUG=True)


