
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


a = Rectangle(3, 2)
print(a.get_area())
print(a.get_perimeter())

b = Rectangle(30, 40)
print(b.get_area())
print(b.get_perimeter())