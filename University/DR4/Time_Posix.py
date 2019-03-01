import time
from datetime import datetime

now = datetime.now()
print(now)
print(now.timetuple())
timestamp = time.mktime(now.timetuple())
print(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
