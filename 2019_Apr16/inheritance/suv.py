from car import Car

class SUV(Car):
    def __init__(self, name):
        Car.__init__(self, name)
        print "SUV init called..."


