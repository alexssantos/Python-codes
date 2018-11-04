import time
import datetime

# --------- TIME Module ---------
format = "%H:%M:%S"                     # Format
print(time.strftime(format))            # 24 hour format #

format = "%I:%M:%S"                     # Format
print(time.strftime(format))            # 12 hour format #

# Date with time-module
format = "%d/%m/%y"
print(time.strftime(format))

input()

# --------- DATETIME Module ---------

now = datetime.datetime.now()
now.hour
now.mintue
now.year
now.day
now.month

date = datetime.now()
print(str(date))
print(date.strftime('%Y/%m/%d %H:%M:%S'))
