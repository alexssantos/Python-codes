import time, datetime

now = datetime.datetime.now()
print(now)
print(time.mktime(now.timetuple()))
