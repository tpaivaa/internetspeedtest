#!/usr/bin/env python3
import time, speedtest, json, datetime, sys, traceback, os, socket
from datetime import timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError, InfluxDBServerError
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
    receiveTime = datetime.datetime.now(datetime.timezone.utc)
    running_hostname = socket.gethostname()

    st = speedtest.Speedtest()
    st.get_best_server()  # Find the best server
    download_bps = st.download()
    upload_bps = st.upload()
    ping = st.results.ping  # Get the ping value

    download_mbps = download_bps / 1000000  # Convert to Mbps
    upload_mbps = upload_bps / 1000000  # Convert to Mbps

    output = {
        "host": running_hostname,
        "download_Mbps": download_mbps,
        "upload_Mbps": upload_mbps,
        "ping_ms": ping,
        "executionSpeed": time.time() - start_time
    }

    json_body = [
        {
            "measurement": 'netSpeed',
            "tags": {
                "hostname": running_hostname
            },
            "time": receiveTime,
            "fields": {
                "download_Mbps": download_mbps,
                "upload_Mbps": upload_mbps,
                "ping_ms": ping
            }
        }
    ]
    dbclient.write_points(json_body)
    print(json.dumps(output, indent=4))

except (InfluxDBClientError, InfluxDBServerError, speedtest.SpeedtestException, socket.error) as e:
  exceptionHandleri(e)
