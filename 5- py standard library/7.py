from datetime import datetime, timedelta
import time
# timedelta is for difference

time.time()
# # floating time (seconds) since beginning of time


dt = datetime(2021, 1, 1) + timedelta(days=1, seconds=1000)

dt2 = datetime.now()

datetime.strptime("2018/01/01", "%Y/%m/%d")

datetime.fromtimestamp(time.time())

dt.year
dt.month
dt.strftime("%Y/%m")

print(dt2 > dt)

# *******************************************

duration = dt2 - dt
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())
