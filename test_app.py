import pytest
from dotenv import load_dotenv
import os
from app import app, create_app
import app
import json
import googlemaps



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
   

def test_get_directions(client):
    response = client.get('/directions/Disneyland/San_Diego')
    my_json = response.data.decode("UTF-8")
    print(my_json)
    data = json.loads(my_json)
    print(data)
    assert response.status_code == 200


def test_invalid_directions(client):
    response = client.get('/directions/Hawaii/San_Diego')
    my_json = response.data.decode("UTF-8")
    print(my_json)
    data = json.loads(my_json)
    print(data)
    assert response.status_code == 404

def test_file_exists():
    assert os.path.exists('./app.py')


def test_file_contents():
    with open('./app.py', 'r') as f:
        contents = f.read()
    assert "api_key" in contents 

def test_config():
    assert not create_app('config').testing
    assert create_app({'TESTING': True})



