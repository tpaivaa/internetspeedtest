# internetspeedtest
Test internetspeed and log to influxdb

# requirements
> Git and Python is needed! Recommend Python3

```
pip3 install Influxdb
pip3 install speedtest-cli
```
# or
> clone the repo and run 
```
git clone https://github.com/tpaivaa/internetspeedtest.git
python3 -m pip install -r requirements.txt
```

# Config file where Influx database parameters in python dictionary
# Just change value to fit your setups
# config.py 
```python
{
  "host":"x.x.x.x",
  "port":"8086",
  "dbuser":"username",
  "dbuser_password":"password",
  "dbname":"database"
}
```
# Use on app.py
```
import config as c

dbclient = InfluxDBClient(c['host'], c['port'], c['dbuser'], c['dbuser_password'], c['dbname'])

```


