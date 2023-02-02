# Flask_Google_API

## Project: Flask & Google API

### Overview
This is a Flask app project that uses a Googlemaps API to generate directions from two locations. A user can submit their requests using a form and have information returned in json format about their destination. The application was unit tested using pytest to test the application functionality. 


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
The purpose of testing this flask application is to test the functionality of the application. The scope of the tests will be to test the data from the googlemaps API, test if files exist, test the http routes, and test the app configuration. The input data will be the starting location and the ending location. The output information will be the json data that we parse from the API. The results of our tests will have a final report. Some constraints are time availability and resource limitations. Some risks include test failures.

### User Story
As a developer, I can connect a google API Key to my Flask app

As a developer, I can submit a request with two inputs that calls the google API

As a developer, I have a route for get json data

As a developer, I want to run unit tests for the data in my flask application, so that issues can be identified and fixed before the application is deployed to production 

As a developer, I want to be able to test that data can be retrieved from the API and that the data is correct 

As a developer, I want 75% minimum test coverage for the backend

### Test Cases
1. Test the data retrieved from the google API 
2. Test file path for files 
3. Test content in files
4. Test the http routes
5. Test invalid inputs
6. Test the app configuration 

### Test Summary
There are 6 pytest tests that passed. The test report and coverage report can be referenced for detailed information about each unit test and overall coverage.

    • Tested feature: Googlemaps API
    • Test environment: Development
    • Test duration: 2 hours
    • Test coverage: 100%
    • Test results: Pass

### Test Cases Executed
```
Test case: Verify the data from the google API
    o Test result: Pass
    o Notes: Tested the data retrieved from API

Test case: Verify file paths exist
    o Test result: Pass
    o Notes: Tested the file path to app.py

Test case: Verify the contents of files
    o Test result: Pass
    o Notes: Tested the contents of the app.py

Test case: Verify http routes work
    o Test result: Pass
    o Notes: Tested the home route and get directions route by verifying status codes and json response data 

Test case: Verify invalid inputs
    o Test result: Pass
    o Notes: Tested by asserting invalid input status code returned 404   

Test case: Verify app configuration
    o Test result: Pass
    o Notes: Tested by asserting app config is true for testing         
    
Test Issues
    • No Issues
    Conclusion: Based on the results of the test cases executed, it can be concluded that the application and google API are functioning as expected. 
```    


#### Testing Report


#### Coverage Report
