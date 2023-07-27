# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:36:47 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Get current time
#------------------------------------------------------------------------------
from datetime import datetime

print(datetime.now())

#------------------------------------------------------------------------------
# Exercise 2 Get current time
#------------------------------------------------------------------------------
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(date_string)

#------------------------------------------------------------------------------
# Exercise 3 Subtract a week (7 days)  from a given date in Python
#------------------------------------------------------------------------------
import datetime as dt

given_date = dt.datetime(2020, 2, 25)
days = dt.timedelta(days=7)

print(given_date - days)

#------------------------------------------------------------------------------
# Exercise 4 Print a date in a the following format Day_name  Day_number  Month_name  Year
#------------------------------------------------------------------------------
import datetime as dt

given_date = datetime(2020, 2, 25)

print(given_date.strftime('%A %d %B %Y'))

#------------------------------------------------------------------------------
# Exercise 5 Find the day of the week of a given date
#------------------------------------------------------------------------------
import datetime as dt

given_date = datetime(2020, 7, 26)

print(given_date.strftime('%A'))

#------------------------------------------------------------------------------
# Exercise 6 Find the day of the week of a given date
#------------------------------------------------------------------------------
# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)

addTime= dt.timedelta(days=7, hours=12)
print(given_date + addTime)

#------------------------------------------------------------------------------
# Exercise 7 Print current time in milliseconds
#------------------------------------------------------------------------------
import time
milli = int(round(time.time() * 1000))
print(milli)

#------------------------------------------------------------------------------
# Exercise 8 Convert the following datetime into a string
#------------------------------------------------------------------------------
import datetime as dt

given_date = datetime(2020, 2, 25)

timeString = given_date.strftime('%Y %m %d')
print(timeString)

#------------------------------------------------------------------------------
# Exercise 9 Calculate the date 4 months from the current date
#------------------------------------------------------------------------------
import datetime as dt
from dateutil.relativedelta import relativedelta
print(datetime(2020, 2, 25).date() + relativedelta(month=4))


#------------------------------------------------------------------------------
# Exercise 10 Calculate number of days between two given dates
#------------------------------------------------------------------------------
import datetime as dt
# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)

result = date_2 - date_1
print(result)

