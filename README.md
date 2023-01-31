# Flask_Google_API

## Project: Flask & Google API

### Overview
A Flask app with an API generated using Googlemaps to generate directions.


### Virtual Environment Installation
1. Create environment: ```python3 -m venv env```
2. Activate environment: ```source env/bin/activate```. (env) indicates environment is active. 
3. run: ```brew install pyenv```. Only needs to be installed once. Check the version of pyenv, run: ```pyenv --version```.
4. If pyenv version not 3.10.7, run: ```pyenv install 3.10.7```
5. Change the local version to 3.10.7, run: ```pyenv local 3.10.7```
6. run: ```pyenv local``` to check the version of pyenv

### Flask Installation
1. Install flask, run: ```pip3 install flask```
2. Create app.py and add imports
3. run: ```export FLASK_APP=app.py```
4. run: ```flask --debug run```, to start the server
5. Create requirements.txt file and add requirements
6. run: ```pip3 install -r requirements.txt```, to install flask, python-dotenv, psycopg2
7. run: ```flask --debug run``` or add FLASK_APP=app, FLASK_DEBUG=1 to .env file to automatically have debugger on. This starts the server

#### Pytest Installation

2. Create requirements.txt file and add requirements
3. run: ```pip3 install -r requirements.txt```, to install requirements
4. run: ```pytest -v -s```, to run tests on application
5. Add pytest-html to requirements.txt file
6. run: ```pip3 install pytest-html```, to install pytest-html
7. run: ```pytest --html=report.html```, this will add report.html file. Open live server to see report of tests
8. run: ```coverage run --omit 'env/*' -m pytest -v -s```, to omit environment from coverage results
9. run: ```coverage report -m```, to get coverage results
10. run: ```coverage html```, to generate htmlcov folder. Then open htmlcov/index.html with live server

### Requirements Gathering for TDD
The purpose of testing this flask application is to test the functionality of the application. The scope of the tests will be to test the data from the googlemaps API, test if files exist, and test the http routes. The input data will be the starting location and the ending location. The output data will be the bson data that parse from the API. The results of our tests will have a final report. Some constraints are time availability and resource limitations. Some risks include test failures.

### User Story
As a developer, I can connect a google API Key to my Flask app.

As a developer, I can submit a request with two inputs that calls the google API

As a developer, I have a route for get json data

As a developer, I want to run unit tests for the data in my flask application, so that issues can be identified and fixed before the application is deployed to production. 

As a developer, I want to be able to test that data can be created and retrieved from the database and that the data is correct. 

As a developer, I have 75% minimum test coverage for the backend

### Test Cases
1. Test the data retrieved from the google API 
2. Test file path for files 
3. Test content in files
4. Test that the http routes work
5. Test response status codes 

### Test Summary
    • Tested feature: Googlemaps API
    • Test environment: Development
    • Test duration: 2 hours
    • Test coverage: 88%
    • Test results: Pass

### Test Cases Executed
```
Test case: Verify the data from the google API
    o Test result: Pass
    o Notes: Tested the data retrieved from API

Test case: Verify data exists in database
    o Test result: Pass
    o Notes: Tested by returning data from db.

Test case: Verify file paths exist
    o Test result: Pass
    o Notes: Tested the file path to app.py and config.py

Test case: Verify the contents of files
    o Test result: Pass
    o Notes: Tested the contents of the app.py and config.py files 

Test case: Verify http routes work
    o Test result: Pass
    o Notes: Tested the home route, get part by id routes, get all parts routes, post part routes, and delete parts by verifying status codes and json response data.      
    
Test Issues
    • No Issues
    Conclusion: Based on the results of the test cases executed, it can be concluded that the database is functioning as expected. 
```    


#### Testing Report


#### Coverage Report
