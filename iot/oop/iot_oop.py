import random
import time
from abc import abstractmethod
from threading import Thread


class Sensor:
    def __init__(self):
        self.type = None

    def get_type(self):
        return self.type

    @abstractmethod
    def get_value(self):
        raise NotImplementedError


class Humidity(Sensor):
    def __init__(self):
        self.type = "Humidity"

    def get_value(self):
        return random.randint(0, 100)


class Temperature(Sensor):
    def __init__(self):
        self.type = "Temperature"

    def get_value(self):
        return random.randint(-10, 40)


class Light(Sensor):
    def get_value(self):
        return random.randint(30, 70)

    def __init__(self):
        self.type = "Light"


class Gas(Sensor):
    def get_value(self):
        return random.randint(0, 10)

    def __init__(self):
        self.type = "Gas"


class Unit:
    def __init__(self, id):
        self.id = id
        self.sensors = []
        self.longitude = None
        self.latitude = None
        self.thread = None

    def set_location(self, lon, lat):
        self.longitude = lon
        self.latitude = lat

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def send_messages(self):
        for sensor in self.sensors:
            message = {"unit": self.id, "longitude": self.longitude, "latitude": self.latitude, "type": sensor.get_type(), "value": sensor.get_value()}
            print(message)

    def move(self):
        while True:
            self.set_location(self.longitude + random.random(), self.latitude + random.random())
            print(self.longitude, self.latitude)
            time.sleep(10)

    def start_moving(self):
        self.thread = Thread(target=self.move)
        self.thread.start()


if __name__ == '__main__':
    units = []
    unit = Unit(1)
    unit.set_location(34.232365, 21.328711)
    unit.add_sensor(Temperature())
    unit.add_sensor(Light())
    units.append(unit)
    unit = Unit(2)
    unit.set_location(35.232365, 20.328711)
    unit.add_sensor(Humidity())
    unit.add_sensor(Gas())
    unit.start_moving()
    units.append(unit)

    for i in range(30):
        for unit in units:
            unit.send_messages()
        time.sleep(20)

