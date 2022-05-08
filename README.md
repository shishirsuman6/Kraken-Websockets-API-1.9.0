# Kraken-Websockets-API-1.9.0
Use the Pytest framework for Kraken Websockets API 1.9.0

Inspection of Websockets API elements for Public Channels:
1. book


## Docker endpoints:
1. Image: Template for running Containers  
Run this on the terminal to build image:  

        docker build -t pytest-kraken-ws .

2. Container: Actual running process where we have our package
Run this on the terminal to start the container: 

        docker run pytest-kraken-ws

## Parallel run using xdist
Configured in [pytest.ini](/pytest.ini)  
The folloiwng options can be used:  
1. Specify number of Parallel runs, e.g. use the following command line flag  

        -n 10  

2. Let Pytest decide the number of Parallel runs using the following command line flag  

        -n auto

## Test Run Reports:
JUnit style XML Report: [report.xml](/report.xml)  
JUnit style XML Report: [report.html](/report.html)  