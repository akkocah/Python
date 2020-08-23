# QUESTION:
# Write Python code to convert below Json data to Python Object, and print this Python Object.

import json
json_car =  '{ "Make":"Mercedes", "Model":"E-200", "Year":2015 }'

car = json.loads(json_car) 
print(car)
print("JSON Data\n", type(car),"\n",car)
print(car.keys())

