class Car:
    
    def __init__(self, name):
        self.name = name
        print "Car", self.name, "created."

    def __del__(self):
        print "Car", self.name, "destroyed"


c1 = Car("Honda")
c2 = c1
c3 = c2
print "Created c1, c2, c3"
del c1
print "c1 deleted..."
del c2
print "c2 deleted..."
#c3 = 100
del c3
print "c3 set to 100..."

