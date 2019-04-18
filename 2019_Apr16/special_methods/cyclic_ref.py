class Car: 
    def __init__(self, name):
        print "Creating car instance", self
        self.name = name

    def __del__(self):
        print "Car destroyed..."

class Person:
    def __init__(self, name):
        self.name = name
        print "Person", self.name, "instantiated."

    def __del__(self):
        print "Person destroyed..."

c1 = Car("Honda")
p1 = Person("Sam")

c1.owner = p1
p1.owns = c1

del p1
del c1
import gc
print gc.collect()
