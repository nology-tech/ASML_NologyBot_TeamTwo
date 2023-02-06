import pytest
from dotenv import load_dotenv
import os
from app import app, create_app
import json
from pytest import approx


load_dotenv() 
api_key = os.getenv("API_KEY") 

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner() 

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_data_types(client):
    response = client.get('/directions/San_Antonio/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(my_json) == str
    assert type(data) == dict
    assert response.status_code == 200    

def test_find_legs(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(data['number of legs']) == int
    assert data['number of legs'] == 1
    assert response.status_code == 200

def test_find_distance(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(data['distance']) == str
    assert data['distance'] == approx("95 mi")
    assert response.status_code == 200

def test_find_time(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert data['time'] == approx("1 hrs")
    assert type(data['time']) == str
    assert response.status_code == 200

def test_find_speed(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(data['speed']) == str
    assert data['speed'] == approx('95 mph')
    assert response.status_code == 200

def test_find_startlatLon(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(data['startLatLon']) == dict
    assert data['startLatLon'] == {"lat": 33.8160897,"lng": -117.9225226}
    assert response.status_code == 200
    
def test_find_endlatLon(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(data['endLatLon']) == dict
    assert data['endLatLon'] == {"lat": 32.7157323, "lng": -117.1610969}
    assert response.status_code == 200    

def test_valid_transportation(client):
    response = client.get('/directions/Florida/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert data['travelModes'] == ['driving']
    assert response.status_code == 200

def test_invalid_transportation(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    assert ['swimming'] not in ['travelModes']
    assert response.status_code == 200    

def test_invalid_directions(client):
    response = client.get('/directions/Hawaii/San_Diego/driving')
    assert b"An error occurred or there are no available directions for this search." in response.data
    assert response.status_code == 404

def test_driving_mode(client):
    response = client.get('/directions/SeaWorld/Los_Angeles/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert len(data['travelModes']) == 1
    assert 'driving' in data['travelModes']
    assert response.status_code == 200

def test_transit_mode(client):
    response = client.get('/directions/SeaWorld/Los_Angeles/transit')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)  
    assert type(data['travelModes']) == list
    assert len(data['travelModes']) == 2
    assert 'transit' and 'walking' in data['travelModes'] 
    assert response.status_code == 200

def test_summary_data(client):
    response = client.get('/directions/SeaWorld/Los_Angeles/transit')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)  
    assert type(data['summary']) == str
    assert data['summary'] == "You will be starting at SeaWorld and walking/taking public transit a total distance of 2690 mi with an average speed of 44 mph until you reach your destination at Los_Angeles."
    assert response.status_code == 200    
      
def test_file_exists():
    assert os.path.exists('./app.py')

def test_file_contents():
    with open('./app.py', 'r') as f:
        contents = f.read()
    assert "api_key" in contents 

def test_config():
    assert not create_app('config').testing
    assert create_app({'TESTING': True})


# @pytest.mark.parametrize("input, expected_output",[
#     (("disneyland_to_seaworld.json"), (49))
# ])
# def test_direc(input, expected_output):
#     # assert 'di' == 49
#     assert add(input[0], input[1]) == expected_output