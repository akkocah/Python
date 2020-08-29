import datetime
from datetime import datetime
try:
    date = input("please enter the date DD-MM-YY :")
    date_obj = datetime.strptime(date, '%d-%m-%Y')
    print(date_obj.strftime('%A'))
    print(date_obj.strftime('%A %B %Y'))
    
except ValueError:
    print("Invalid date.")

#########################################################

import pandas as pd
try:
    date = input("please enter the date DD-MM-YY :")
    df = pd.Timestamp(date)
    print(df.dayofweek, df.day_name())
except ValueError:
    print("Invalid date.")
######################################################

from datetime import datetime
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
while True:
    try:
        date1 = datetime.strptime(input('Please enter a date in "Month/Day/Year" format: '),'%m/%d/%Y')
    except:
        print('Your input is not a valid date')
    else:
        print(f"{date1.date()} is {weekDays[date1.weekday()]}")

###################################################################

import datetime
def is_date_valid():
    try:
        date = input("Please enter a valid date (DD-MM-YYYY): ")
        conv_date = datetime.datetime.strptime( date, "%d-%m-%Y" )
        print(conv_date)
    except Exception as e:
        print ('Exception type is:', e.__class__.__name__)
        # print_exc()
        return print("Invalid Entry")
    else:
        return print(conv_date.strftime("%A"))



