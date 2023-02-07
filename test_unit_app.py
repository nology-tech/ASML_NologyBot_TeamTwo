import pytest
from dotenv import load_dotenv
import os
from app import *
import json
from pytest import approx
import logging
from datetime import date

with open('./data.json', 'r') as f:
  data = json.load(f)
  
def test_find_legs_unit():
  response = find_legs(data)
  assert response == 1
  
def test_find_distance_unit():
  response = find_distance(data)
  assert response == "94 mi"

def test_find_time_unit():
  response = find_time(data)
  assert response == "1 hrs"
  
def test_find_speed_unit():
  response = find_speed(data)
  assert response == "94 mph"

def test_find_startLatLon_unit():
  response = find_startLatLon(data)
  assert response == {"lat": 32.7157323, "lng": -117.1610969}
  
def test_find_endLatLon_unit():
  response = find_endLatLon(data)
  assert response == {"lat": 33.8160897, "lng": -117.9225226}

def test_find_travelModes_unit():
  response = find_travelModes(data)
  assert response == ["driving"]

def test_create_summary_unit():
  start = "San Diego, CA, USA"
  end = "1313 Disneyland Dr, Anaheim, CA 92802, USA"
  response = create_summary(data,start, end)
  assert response == "You will be starting at San Diego, CA, USA and driving a total distance of 94 mi with an average speed of 94 mph until you reach your destination at 1313 Disneyland Dr, Anaheim, CA 92802, USA."