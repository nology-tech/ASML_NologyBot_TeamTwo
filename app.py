from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import googlemaps
import json
from functions import *

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
            return json.dumps({"number of legs": find_legs(directions_result),
                                "distance": find_distance(directions_result),
                                "time": find_time(directions_result),
                                "speed": find_speed(directions_result),
                                "startLatLon": find_startLatLon(directions_result),
                                "endLatLon": find_endLatLon(directions_result),
                                "travelModes": find_travelModes(directions_result),
                                "summary": create_summary(directions_result, x, y)}, indent=4), 200
        else:
            return json.dumps({"error": "An error occurred or there are no available directions for this search."}), 404


    @app.route("/alternative-directions/<x>/<y>", methods=["GET"])
    def get_alternative_directions(x, y):
        directions_result = gmaps.directions(origin = x, destination = y, alternatives = True)
        if directions_result:
            return directions_result, 200
        else:
            return json.dumps({"error": "An error occurred or there are no available directions for this search."}), 404


    @app.route("/waypoint-directions/<x>/<y>/<z>", methods=["GET"])
    def get_waypoint_directions(x, y, z):
        directions_result = gmaps.directions(origin = x, destination = y, waypoints = z, optimize_waypoints = True)
        if directions_result:
            return directions_result
        else:
            return json.dumps({"error": "An error occurred or there are no available directions for this search."}), 404 
    
    @app.route("/avoid-directions/<x>/<y>/<a>", methods=["GET"])
    def get_avoid_directions(x, y, a):
        directions_result = gmaps.directions(origin = x, destination = y, avoid = a)
        if directions_result:
            return directions_result
        else:
            return json.dumps({"error": "An error occurred or there are no available directions for this search."}), 404        
    
    @app.route("/transit-directions/<x>/<y>/<t>", methods=["GET"])
    def get_transit_directions(x, y, t):
        directions_result = gmaps.directions(origin = x, destination = y, mode = "transit", transit_mode = t)
        if directions_result:
            return directions_result
        else:
            return json.dumps({"error": "An error occurred or there are no available directions for this search."}), 404

    return app

app = create_app({"TESTING": False})

if __name__ == "__main__":  #pragma: no cover
    app.run(DEBUG=True)


