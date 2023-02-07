# import logging
# import pytest
# from dotenv import load_dotenv
# import os
# from app import app, create_app
# import json
# from pytest import approx

# log_format = '%(asctime)s   %(name)s    %(levelname)s    %(message)s'
# logger = logging.getLogger(__name__)
# logger.setLevel('DEBUG')
# file_handler = logging.FileHandler("test_app.log")
# formatter = logging.Formatter(log_format)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# load_dotenv() 
# api_key = os.getenv("API_KEY") 

# # @pytest.fixture
# # def app():
# #     app = create_app({"TESTING": True})
# #     app.config.update({
# #         "TESTING": True,
# #     })
# #     yield app

# # @pytest.fixture
# # def client(app):
# #     return app.test_client()

# # @pytest.fixture()
# # def runner(app):
# #     return app.test_cli_runner() 

# def test_home_page(client):
#     logger.info('Testing home route')
#     response = client.get('/')
#     assert response.status_code == 200

# def test_data_types(client):
#     logger.info('Testing data types of decoded json object')
#     response = client.get('/directions/San_Antonio/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(my_json) == str
#     assert type(data) == dict
#     assert response.status_code == 200 

# def test_find_legs(client):
#     logger.info('Testing find legs')
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['number of legs']) == int
#     assert data['number of legs'] == 1
#     assert response.status_code == 200   

# def test_find_distance(client):
#     logger.info('Testing find distance')
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['distance']) == str
#     assert data['distance'] == approx("95 mi")
#     assert response.status_code == 200

# def test_find_time(client):
#     logger.info('Testing find time')
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['time']) == str
#     assert data['time'] == approx("1 hrs")
#     assert response.status_code == 200

# def test_find_speed(client):
#     logger.info('Testing find speed')
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['speed']) == str
#     assert data['speed'] == approx('95 mph')
#     assert response.status_code == 200

# def test_find_startlatLon(client):
#     logger.info('Testing find startlatLon')
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['startLatLon']) == dict
#     assert data['startLatLon'] == {"lat": 33.8160897,"lng": -117.9225226}
#     assert response.status_code == 200
   
# def test_find_endlatLon(client):
#     logger.info('Testing find endlatLon') 
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['endLatLon']) == dict
#     assert data['endLatLon'] == {"lat": 32.7157323, "lng": -117.1610969}
#     assert response.status_code == 200    

# def test_valid_transportation(client):
#     logger.info('Testing Florida to San Diego travel mode')
#     response = client.get('/directions/Florida/San_Diego/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert data['travelModes'] == ['driving']
#     assert response.status_code == 200

# def test_invalid_transportation(client):
#     logger.info('Testing Disneyland to San Diego invalid travel mode')
#     response = client.get('/directions/Disneyland/San_Diego/driving')
#     assert ['swimming'] not in ['travelModes']
#     assert response.status_code == 200    

# def test_invalid_directions(client):
#     logger.info('Testing invalid directions status code 404')
#     response = client.get('/directions/Hawaii/San_Diego/driving')
#     assert b"An error occurred or there are no available directions for this search." in response.data
#     assert response.status_code == 404

# def test_driving_mode(client):
#     logger.info('Testing Seaworld to Los Angeles driving mode')
#     response = client.get('/directions/SeaWorld/Los_Angeles/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)
#     assert type(data['travelModes']) == list
#     assert len(data['travelModes']) == 1
#     assert 'driving' in data['travelModes']
#     assert response.status_code == 200

# def test_transit_mode(client):
#     logger.info('Testing Seaworld to Los Angeles transit mode')
#     response = client.get('/directions/SeaWorld/Los_Angeles/transit')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)  
#     assert type(data['travelModes']) == list
#     assert len(data['travelModes']) == 2
#     assert 'transit' and 'walking' in data['travelModes'] 
#     assert response.status_code == 200

# def test_summary_data_driving(client):
#     logger.info('Testing summary of driving directions')
#     response = client.get('/directions/SeaWorld/Los_Angeles/driving')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)  
#     assert type(data['summary']) == str
#     speed = approx(data['speed'])
#     distance = approx(data['distance'])
#     assert data['summary'] == f"You will be starting at SeaWorld and driving a total distance of {distance} with an average speed of {speed} until you reach your destination at Los_Angeles."

# def test_summary_data_transit(client):
#     logger.info('Testing summary of transit directions')
#     response = client.get('/directions/SeaWorld/Los_Angeles/transit')
#     my_json = response.data.decode("UTF-8")
#     data = json.loads(my_json)  
#     assert type(data['summary']) == str
#     speed = approx(data['speed'])
#     distance = approx(data['distance'])
#     assert data['summary'] == f"You will be starting at SeaWorld and walking/taking public transit a total distance of {distance} with an average speed of {speed} until you reach your destination at Los_Angeles."
#     assert response.status_code == 200    

# def test_file_exists():
#     logger.info('Testing file path to app exists') 
#     assert os.path.exists('./app.py')

# def test_file_contents():
#     logger.info('Testing file contents of app')
#     with open('./app.py', 'r') as f:
#         contents = f.read()
#     assert "api_key" in contents 

# def test_config():
#     logger.info('Testing config of app')
#     assert not create_app('config').testing
#     assert create_app({'TESTING': True})
