
class Vehicle:
    def __init__(self, brand, plate, length):
        print('Constructor called')
        self.brand = brand
        self.plate = plate
        self.length = length

    def display(self):
        print(self.brand + " " + self.plate + " " + str(self.length))

    def __str__(self):
        return "Vehicle: " + self.brand + " " + self.plate + " " + str(self.length)


a = Vehicle("VW", "ZAB5467", 5.34)
b = Vehicle("Audi", "AXN7812", 6.28)
c = Vehicle(b.brand, b.plate, b.length)
c.plate = "AAN6123"

print(a)
print(b)
print(c)


