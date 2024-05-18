from opensky_api import OpenSkyApi
import pandas as pd
from influxdb_client  import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime, timezone
import time
import secret

db = "flightdata"
url= "https://us-east-1-1.aws.cloud2.influxdata.com/"
#token and org are stored in secret.py - please create this file for yourself 
influxdbClient = InfluxDBClient(url=url, token=secret.token, org=secret.org)
write_api = influxdbClient.write_api(write_options=SYNCHRONOUS)


# FLIGHTS data
api = OpenSkyApi()
# This is the denver area
states = api.get_states(bbox=((39.368093, 40.186033, -105.478063, -104.258580)))

#we set these values to 0 to start the loop
total_row = 0
batch = 0
df_list = []


while True:
    timestamp = str(datetime.now(timezone.utc))
    total_row = 0
    for s in states.states:
            if batch == 50:
                concatenated = pd.concat(df_list).infer_objects().ffill()
                # Fill NaN values with "None", influxdb does not like NaN values
                concatenated['sensors'] = concatenated['sensors'].fillna("None")
        
                concatenated = concatenated.convert_dtypes()
                batch = 0
                df_list = []
                   
                try: 
                    print("here")
                    concatenated['time'] = pd.to_datetime(concatenated['time'])
                    write_api.write(bucket=db, record=concatenated, data_frame_measurement_name='flight', data_frame_tag_columns=['icao24', 'origin_country'], data_frame_timestamp_column='time' )
                except:
                    total_row -= 50
            else:
                df = pd.DataFrame.from_dict(s.__dict__, orient='index' ).T
                df['time'] = timestamp
                df_list.append(df)
                batch += 1
                total_row += 1
                             
            
    print(f"Inserted {total_row} rows")
    # Sleep for 1 minute to avoid rate limiting
    time.sleep(60)