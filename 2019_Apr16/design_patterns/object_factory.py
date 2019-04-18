def create(objtype, name=None):
    if objtype == "car":
        class Car:
            def __init__(self, name):
                self.name = name
            def drive(self):
                print "Driving car: ", self.name

        return Car(name)

    elif objtype == "bike":
        class Bike:
            def ride(self):
                print "Riding a bike..."
        return Bike()

    elif objtype == "plane":
        class Plane:
            def fly(self):
                print "Flying a plane..."
        return Plane()

c = create("car", "honda") 
c.drive()
print c.__class__.__name__


b = create("bike")
b.ride()
print b.__class__.__name__

f = create("plane")
f.fly()


