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

    @app.route("/directions/<x>/<y>", methods=["GET"])
    def get_directions(x, y):
        directions_result = gmaps.directions(origin = x, destination = y)
        if directions_result:
            return create_summary(directions_result, x, y), 200
        else:
            return json.dumps({"error": "Cannot find directions. Enter a drivable route!"}), 404


    def create_summary(directions, origin, destination):
        distance = math.floor(directions[0]["legs"][0]["distance"]["value"]/1609.34)
        time = math.floor(directions[0]["legs"][0]["duration"]["value"]/3600)
        speed = distance/time
        endLatLon = directions[0]["legs"][0]["end_location"]
        startLatLon = directions[0]["legs"][0]["start_location"]
        modeOfTravel = directions[0]["legs"][0]["steps"][0]["travel_mode"]
        summary = f"You will be starting at {origin} and {modeOfTravel.lower()} a total distance of {distance} miles with an average speed of {speed} mph until you reach your destination at {destination}."

        return json.dumps({"number of legs": len(directions[0]["legs"]),
                            "distance traveled": f"{distance} mi",
                            "travel time": f"{time} hrs",
                            "average speed": f"{speed} mph",
                            "startLatLon": startLatLon,
                            "endLatLon": endLatLon,
                            "travel mode": modeOfTravel,
                            "summary of trip": summary
        }, indent=4)

    return app

app = create_app({"TESTING": False})

if __name__ == "__main__":
    app.run(DEBUG=True)


