# QUESTION:
# Write a Python code to find how many days passed from "2020-5-31" to today.

from datetime import date
delta = date.today() - date(2020,5,31)
print(delta.days)

#############################
from datetime import date
day = date(2020,5,31)
today = date(2020,8,28)
a = date.toordinal(today)-date.toordinal(day)
print(a)

##############################
from datetime import datetime as dt
print(dt.today().toordinal()-dt.strptime('2020-05-31', '%Y-%m-%d').date().toordinal())
