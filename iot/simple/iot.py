import random

units = []

unit1 = ["35.234465", "21.341221", "Temperature", "Humidity", "Light"]
unit2 = ["35.234465", "21.341221", "Wind", "Gas", "UV"]
units.append(unit1)
units.append(unit2)

counter = 0
for unit in units:
    counter += 1
    for sensor in unit:
        message = ''
        if sensor == "Temperature":
            message = {"unit": counter, "longitude": unit[0], "latitude": unit[1], "type": "temperature", "value": random.randint(-10, 40)}
        elif sensor == "Humidity":
            message = {"unit": counter, "longitude": unit[0], "latitude": unit[1], "type": "humidity", "value": random.randint(0, 100)}
        elif sensor == "Light":
            message = {"unit": counter, "longitude": unit[0], "latitude": unit[1], "type": "light", "value": random.randint(0, 100)}
        elif sensor == "Wind":
            message = {"unit": counter, "longitude": unit[0], "latitude": unit[1], "type": "wind", "value": random.randint(0, 30)}
        elif sensor == "Gas":
            message = {"unit": counter, "longitude": unit[0], "latitude": unit[1], "type": "Gas", "value": random.randint(0, 100)}
        elif sensor == "UV":
            message = {"unit": counter, "longitude": unit[0], "latitude": unit[1], "type": "uv", "value": random.randint(0, 100)}
        if len(message) > 0:
            print(message)

