# In the Gregorian calendar, three criteria must be taken into account to 
# identify leap years:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year; unless...
# The year is also evenly divisible by 400. Then it is a leap year.
# According to these rules, the years 2000 and 2400 are leap years, 
# while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.

year = int(input("Yılı giriniz :"))
leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
result = (leap_year == True)*'artık yıldır.' + (leap_year == False)*'artık yıl değildir.'

print(f"girdiğiniz *{year:^8}* senesi {result:^16}!")