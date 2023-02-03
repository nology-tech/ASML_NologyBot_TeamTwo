import pytest
from dotenv import load_dotenv
import os
from app import app, create_app
import json


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
    
def test_valid_transportation(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert data['travel mode'] == ['driving']
    assert response.status_code == 200

def test_invalid_transportation(client):
    response = client.get('/directions/Disneyland/San_Diego/driving')
    assert ['swimming'] not in ['travel mode']
    assert response.status_code == 200    

def test_invalid_directions(client):
    response = client.get('/directions/Hawaii/San_Diego/driving')
    assert b"An error occurred or there are no available directions for this search." in response.data
    assert response.status_code == 404

def test_data_types(client):
    response = client.get('/directions/San_Antonio/San_Diego/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert type(my_json) == str
    assert type(data) == dict
    assert type(data['number of legs']) == int
    assert type(data['distance traveled']) == str
    assert type(data['travel time']) == str
    assert type(data['average speed']) == str
    assert type(data['startLatLon']) == dict
    assert type(data['endLatLon']) == dict
    assert type(data['travel mode']) == list
    assert type(data['summary of trip']) == str
    assert response.status_code == 200  

def test_driving_mode(client):
    response = client.get('/directions/SeaWorld/Los_Angeles/driving')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)
    assert data['number of legs'] == 1
    assert data['startLatLon'] == {"lat": 28.4078434, "lng": -81.4674182}   
    assert data['endLatLon'] == {"lat": 34.0523525, "lng": -118.2435717}
    assert len(data['travel mode']) == 1
    assert  'driving' in data['travel mode']
    assert 'travel time' in my_json
    assert response.status_code == 200

def test_transit_mode(client):
    response = client.get('/directions/SeaWorld/Los_Angeles/transit')
    my_json = response.data.decode("UTF-8")
    data = json.loads(my_json)  
    assert data['number of legs'] == 1
    assert data['startLatLon'] == {"lat": 28.4116151, "lng": -81.4639195}   
    assert data['endLatLon'] == {"lat": 34.0338675, "lng": -118.2357129}
    assert len(data['travel mode']) == 2
    assert 'transit' and 'walking' in data['travel mode'] 
    assert 'summary of trip' in my_json
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


