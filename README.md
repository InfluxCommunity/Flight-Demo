# FlightAware Data Fetcher

This Python script fetches flight data from the FlightAware API and stores it in an InfluxDB database.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3
- pandas
- requests
- [influxdb_client_3](https://github.com/InfluxCommunity/influxdb3-python)
- [Flight Aware API](https://www.flightaware.com/commercial/aeroapi/)
- [InfluxDB v3](https://www.influxdata.com/)
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

## Things to Note

1. The test files can be used to test a json file and input into influxdb before you start calling the API for real. Make sure you are happy with the data you are sending in first. 
2. The JSON file can be uploaded into Grafana and if you choose to send the same data as me should populate effectivley. 

## Work to be done
1. Change the open sky API to be the new influxdb v3 python library instead of v2. 
2. Submit this project to flight aware so they can use it as an example
3. Attach all the youtube video into this read me. 
4. Add instructions on how to run this on github actions
5. Add real test files
6. Find a good way to save and use the way points. 
7. Create other front ends for the project in superset, etc. 