# Kraken-Websockets-API-1.9.0

## Summary
This is a repository of example on how to use the Python and Pytest framework for validating [Kraken Websockets API 1.9.0](https://docs.kraken.com/websockets/).  
It covers the folloiwng:  
1. Connection to Kraken Websockets API.
2. Assert details on Public Channel messages (Request and Reponse).
3. Run Test in pralle mode.
4. Provide Docker endpoints for ease of installations and execution via container.
5. Generate HTML and XML reports of Test run results.

## Test Scenarios:

|__Public Channel Name__|__Test Scenario__|__Status__|
|-----------|-----------|-----------|
|Book|1. Validate Publication Payload elements |Completed |
| |2. Validate whether Book publication has Ask price updates in the last t seconds (configurable) |Completed|Completed |
| |3. Validate whether Book publication has Bid price updates in the last t seconds (configurable) |Completed|
| |4. Validate Response Schema- subscriptionStatus|Completed|
| |5. Validate Response Schema- book publication snapshot |Completed|
| |6. Validate Response Schema- book publication update |Completed|
| |7. Validate Invalid Request |Completed|
| |8. Validate Server heartbeat sent more than once within the last 2 seconds |Completed|
|ticker|1. Validate Response Schema- publication | |
|ohlc|1. Validate Response Schema- publication | |
|trade|1. Validate Response Schema- publication | |
|spread|1. Validate Response Schema- publication | |
|General Message|1. Validate payload elements of Status sent on connection or system status changes.|Completed|
||2. Validate system status Response Schema|Completed|
||3. Validate server Ping Response with or without optional request fields|Completed|
||4. Validate server Ping Response Schema|Completed|
||5. Validate server Ping for various Invalid Requests|Completed, see Notes 1 below|

Notes 1: Requires further evaluation for an unexpected observation. Details are noted in [test_kraken_websocket_api.py](/tests/test_kraken_websocket_api.py): test_ping_response_error_reqid  

## Docker endpoints:
Pre-requisite:
1. [Install Docker](https://www.docker.com/get-started/) for the end user Operating System.  
2. Clone this repository.  
3. Launch the terminal/command prompt and navigate to the folder for this repository.  

After that, follow these steps: 
1. Image: Template for running Containers. Run the following on the terminal to build image:  

        docker build -t pytest-kraken-ws .

2. Container: Actual running process where we have our package. Run the following on the terminal to start the container:  

        docker run pytest-kraken-ws

## Parallel run using xdist
Configured in [pytest.ini](/pytest.ini)  
The folloiwng options can be used:  
1. Let Pytest decide the number of Parallel runs using the following command line flag  
This option is built into the Docker Image by default.

        -n auto

2. Specify number of Parallel runs, e.g. use the following command line flag:  
To use this option, make changes in the [pytest.ini](/pytest.ini) file.  

        -n 10  

Note: Docker image would require to be re-built if parallel run change are made.

## Test Run Reports:
JUnit style XML Report: [Test_Run_Report.xml](/Test_Run_Report.xml)  
JUnit style XML Report: [Test_Run_Report.html](/Test_Run_Report.html)  

Command to generate: python -m pytest  