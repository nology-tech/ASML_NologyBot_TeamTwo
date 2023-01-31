from flask import Flask, request
from dotenv import load_dotenv
import os
import googlemaps
import json
import math

load_dotenv() 
api_key = os.getenv("API_KEY") 
app = Flask(__name__)
gmaps = googlemaps.Client(key=api_key)

@app.route("/directions/<x>/<y>", methods=["GET"])
def get_directions(x, y):
    directions_result = gmaps.directions(origin = x, destination = y)
    if directions_result:
        return create_summary(directions_result), 200
    else:
        return json.dumps({"error": "Cannot find directions. Enter a drivable route!"}), 404

def create_summary(directions):
    distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
    time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
    speed = distance/time
    endLatLon = directions[0]["legs"][0]["end_location"]
    startLatLon = directions[0]["legs"][0]["start_location"]
    modeOfTravel = directions[0]["legs"][0]["steps"][0]["travel_mode"]

    return json.dumps({"number of legs": len(directions[0]["legs"]),
                        "distance traveled": f"{distance} mi",
                        "travel time": f"{time} hrs",
                        "average speed": f"{speed} mph",
                        "startLatLon": startLatLon,
                        "endLatLon": endLatLon,
                        "travel mode": modeOfTravel
    }, indent=4)

if __name__ == "__main__":
    app.run(DEBUG=True)