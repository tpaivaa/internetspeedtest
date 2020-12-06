# internetspeedtest
Test internetspeed and log to influxdb

# requirements
# Config file where Influx database parameters in python dictionary
# Just change value to fit your setups
# config.py 
```python
{
  "host":"x.x.x.x",
  "port":"8086",
  "dbuser":"username",
  "dbuser_password":"password"
}
```
# Use on app.py
```
import config as c

dbclient = InfluxDBClient(c.host, c.port, c.user, c.password, c.dbname)

```


