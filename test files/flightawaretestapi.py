import requests
import pandas as pd
import numpy as np
import polars as polars
from influxdb_client_3  import InfluxDBClient3
from datetime import datetime,timezone
import secret
import time
import json


# THIS IS A TEST FILE, FOR TESTING THE JSON FILE

db = "flightawaredata"
url= "https://us-east-1-1.aws.cloud2.influxdata.com/"

#token and org are stored in secret.py - please create this file for yourself 
influxdbClient = InfluxDBClient3(host=url, token=secret.tokenflightaware, org=secret.org)


def convert_to_utc(timestamp):
    if timestamp is not None:
        return str(datetime.now(timezone.utc))
    else:
        return "null"

flight_list = []
total_row = 0
flight_data=[]

with open('test.json') as file:
    data = json.load(file)

    for flight in data["flights"]:
        # smaller planes and private jets dont have to declare their destination, for a first run im removing these
        if flight['destination'] is not None:
            print(convert_to_utc(flight['last_position']['timestamp']))
            flight_data.append({
                "ident": flight['ident'],
                "fa_flight_id": flight['fa_flight_id'],
                "takeoff_time": convert_to_utc(flight['actual_off']),
                "landing_time": convert_to_utc(flight['actual_on']),
                "first_position_time": convert_to_utc(flight['first_position_time']),
                # we are setting this one for the time value, which is required
                "last_position": convert_to_utc(flight['last_position']['timestamp']),
                "altitude": flight['last_position']['altitude'],
                "altitude_change": flight['last_position']['altitude_change'],
                "groundspeed": flight['last_position']['groundspeed'],
                "latitude": flight['last_position']['latitude'],
                "longitude": flight['last_position']['longitude'],
                "aircraft_type": flight['aircraft_type']
            })
            #we want every value in the origin and destination - in the future im going to reduce this down to less codes and such
            for key,value in flight['origin'].items():
                flight_data.append({f"origin_{key}": value})
            else:
                flight_data.append({})

            for key,value in flight['destination'].items():
                flight_data.append({f"destination_{key}": value})
            else:
                flight_data.append({})

           # this is the break up of the waypoints first and last. Its not impossible to store them all, I just dont know a good way yet.
            waypoints = flight['waypoints']
            waypoints = list(zip(waypoints[::2], waypoints[1::2]))

            if waypoints:
                first_waypoint = waypoints[0]
                last_waypoint = waypoints[-1]
                flight_data.append({"First Waypoint": {"Latitude": first_waypoint[0], "Longitude": first_waypoint[1]}})
                flight_data.append({"Last Waypoint": {"Latitude": last_waypoint[0], "Longitude": last_waypoint[1]}})
            
            # this is for me to look at in the console later!
            print(flight_data)
            # Merge all dictionaries into one
            merged_data = {}
            for d in flight_data:
                merged_data.update(d)
            flight_df = pd.DataFrame([merged_data])
            flight_df['timestamp'] = flight_df['last_position']
            influxdbClient._write_api.write(bucket=db, record=flight_df, data_frame_measurement_name='flight', data_frame_tag_columns=['ident', 'fa_flight_id'], data_frame_timestamp_column='timestamp')
            total_row += 1