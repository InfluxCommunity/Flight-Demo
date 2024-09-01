# FlightAware Data Fetcher

This Python script fetches flight data from the FlightAware API and stores it in an InfluxDB database. This is made for InfluxDB cloud v3 for Flight aware API. Flight Aware is a very popular flight data aggregator. Its a common tool in the aviation industry, and for myself its where I go to find out information about my own upcoming flights. 

We have some code for the Open Sky API using InfluxDB v2, the Open Sky API is not updated very often and is probably not ideal for use with a time series database. 

### Prerequisites

What things you need to install the software and how to install them:

- Python 3
- pandas
- requests
- [influxdb_client_3](https://github.com/InfluxCommunity/influxdb3-python)
- [Flight Aware API](https://www.flightaware.com/commercial/aeroapi/)
- [InfluxDB v3 Token](https://www.influxdata.com/)
- Optional[Grafana Dashboard](https://grafana.com/)
- Optional [Open Sky API](https://openskynetwork.github.io/opensky-api/)

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository
2. Install dependencies with `pip install pandas requests influxdb3-python`
3. Create a `secret.py` file with your FlightAware API key and InfluxDB token
4. Run the script with `python flightAware.py`

## Running the script

The script runs in an infinite loop, fetching flight data every 5 minutes, you could make it shorter or longer, but this API is not free. It fetches data for flights within a specified bounding box and stores the data in an InfluxDB database. There is a link to a website to create your own boundbox, for example where you live.

## Youtube resources
These are a collection of youtube videos that go over this project more in depth.  
- [Building the Grafana Dashboard](https://youtu.be/AnVUiUClmfw)
- [Building the Grafana Dashboard with Variables](https://youtu.be/4JeUZzho2ZU)
- [Building Alerting in Grafana](https://youtu.be/jyfG0u9w5Co)
- Coming soon [Basic Python/InfluxDB Tutorial] - Based off this project
- Coming soon [FlightAware and InfluxDB] - Walkthrough of the project
- Coming soon [Running Python Script on Github actions] Based off this project

## Things to Note

1. The test files can be used to test a json file and input into influxdb before you start calling the API for real. Make sure you are happy with the data you are sending in first. 
2. The JSON file can be uploaded into Grafana and if you choose to send the same data as me should populate effectivley. 

## Work to be done
1. Change the open sky API to be the new influxdb v3 python library instead of v2. 
2. Submited this project to flight aware so they can use it as an example[https://github.com/flightaware/aeroapps/issues/18]
3. Add instructions on how to run this on github actions
4. Add real test files
5. Find a good way to save and use the way points. 
6. Create other front ends for the project in superset, etc. 
