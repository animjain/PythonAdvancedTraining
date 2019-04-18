class Person:
    def __init__(self):
        print ("person object created")

    def __del__(self):
        print("person object deleted")


class Car:
    def __init__(self):
        print("Car object created")

    def __del__(self):
        print("Car object deleted")

c = Car()
p = Person()

c.perspn  = p
p.car = c

del p