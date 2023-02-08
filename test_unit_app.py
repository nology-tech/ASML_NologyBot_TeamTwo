from app import *
import json
import logging

log_format = '%(asctime)s    %(name)s    %(levelname)s    %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler = logging.FileHandler("test_app.log")
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

with open('./data.json', 'r') as f:
  data = json.load(f)
  
def test_find_legs_unit():
  logger.info('Unit testing find legs')
  response = find_legs(data)
  assert response == 1
  
def test_find_distance_unit():
  logger.info('Unit testing find distance')
  response = find_distance(data)
  assert response == "94 mi"

def test_find_time_unit():
  logger.info('Unit testing find time')
  response = find_time(data)
  assert response == "1 hrs"
  
def test_find_speed_unit():
  logger.info('Unit testing find speed')
  response = find_speed(data)
  assert response == "94 mph"

def test_find_startLatLon_unit():
  logger.info('Unit testing find startLatLon')
  response = find_startLatLon(data)
  assert response == {"lat": 32.7157323, "lng": -117.1610969}
  
def test_find_endLatLon_unit():
  logger.info('Unit testing find endlatLon') 
  response = find_endLatLon(data)
  assert response == {"lat": 33.8160897, "lng": -117.9225226}

def test_find_travelModes_unit():
  logger.info('Unit testing travel mode')
  response = find_travelModes(data)
  assert response == ["driving"]

def test_create_summary_unit():
  logger.info('Unit testing summary of transit directions')
  start = "San Diego, CA, USA"
  end = "1313 Disneyland Dr, Anaheim, CA 92802, USA"
  response = create_summary(data,start, end)
  assert response == "You will be starting at San Diego, CA, USA and driving a total distance of 94 mi with an average speed of 94 mph until you reach your destination at 1313 Disneyland Dr, Anaheim, CA 92802, USA."

def test_file_exists():
    logger.info('Unit testing file path to app exists') 
    assert os.path.exists('./app.py')

def test_file_contents():
    logger.info('Unit testing file contents of app')
    with open('./app.py', 'r') as f:
        contents = f.read()
        assert "api_key" in contents   


