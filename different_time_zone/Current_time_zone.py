# how to read the different  time_zone using  python module
# we import the datetime class from the datetime module.
from datetime import datetime

# we import the module pytz which is help us to ready different time zone
import pytz
# let see the read the timezone Newyork
tz_NY = pytz.timezone('America/New_york')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

# let see the read the timezone Europe_London
tz_NY = pytz.timezone('Europe/London')
datetime_NY = datetime.now(tz_NY)
print("London time:", datetime_NY.strftime("%H:%M:%S"))

# let see the read the timezone Europe_london
tz_NY = pytz.timezone('Africa/Cairo')
datetime_NY = datetime.now(tz_NY)
print("Cairo:", datetime_NY.strftime("%H:%M:%S"))
