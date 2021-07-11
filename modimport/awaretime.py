import datetime
import pytz

local_time = datetime.datetime.now()
utc_time= datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("aware local time {}".format(aware_local_time))
print("aware UTC {}".format(aware_utc_time))

gap_time = datetime.datetime(2021, 12, 6, 12, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 126745637262
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone()
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone()
print(dt1)
print(dt2)
