from flask import Flask, request
from dotenv import load_dotenv
import os
import googlemaps
from datetime import datetime

load_dotenv() 
api_key = os.getenv("API_KEY") 
app = Flask(__name__)
gmaps = googlemaps.Client(key=api_key)
now = datetime.now()

@app.route("/directions/<x>/<y>")
def get_directions(x, y):
    directions_result = gmaps.directions(origin = x, destination = y, departure_time=now)
    return directions_result

if __name__ == "__main__":
    app.run(DEBUG=True)