class Car:
    def __init__(self, name):  # initializer method
        self.name = name

    def __str__(self):
        return "Car object of name " + self.name

c1 = Car("Honda")
c2 = Car("Toyota")

print c1
print c2
