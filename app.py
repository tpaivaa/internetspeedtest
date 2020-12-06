#!/usr/bin/env python3
import time, speedtest, json, datetime, sys, traceback, os
from datetime import timedelta
from influxdb import InfluxDBClient
from config import influxDBconfig as c

def exceptionHandleri(e):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exc(limit=2, file=sys.stdout)
    print(repr(traceback.extract_tb(exc_traceback)))
    print(exc_type, exc_value)
    print('Ja se Error: ', e)

try:
  dbclient = InfluxDBClient(c['host'], c['port'], c['dbuser'], c['dbuser_password'], c['dbname'])
  start_time = time.time()
  receiveTime=datetime.datetime.utcnow()
  #
  # Perform computations.
  #
  
  st = speedtest.Speedtest()
  st.get_best_server()
  download = st.download()
  elapsed_time_secs = time.time() - start_time
  output =  {"download": str(download) , "executionSpeed" : str(elapsed_time_secs) }

  json_body = [
    { "measurement": 'netSpeed',
      "time": receiveTime,
      "fields": {
          "value": download
      }
    }
  ]
  dbclient.write_points(json_body)
  print (json.dumps(output, indent=4))

except Exception as e:
  exceptionHandleri(e)