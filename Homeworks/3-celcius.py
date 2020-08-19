#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# celsius = float(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

# celsius_temp = 41
# fahrenheit_temp = (celsius_temp * 9/5) + 32

# #result = "%.2f Celsius Degree equal = %.2f Farenheit Degree" %(celsius_temp, fahrenheit_temp)

# result = f"{celsius_temp :.2f} Celsius Degree equal = {fahrenheit_temp:0.2f} Farenheit Degree"

# #result = "{:.2f} Celsius Degree equal = {:.2f} Farenheit Degree ".format(celsius_temp, fahrenheit_temp)

# print(result)

#km = float(input("Mesafe kaç km : "))
km = 1000
mil = (km / 1.852)
#result = "%.2f Kilometers equal = %.2f miles" %(km, mil)
#result = "{:0.2f} Kilometers equal = {:0.2f} miles".format(km, mil) 
result = f"{km:0.2f} Kilometers equal = {mil:0.2f} miles"

print(result)









