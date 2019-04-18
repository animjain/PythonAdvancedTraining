class Car(object):
    def __init__(self, name):
        print "Car object created..."
        self.name = name


class SUV(Car):
    #def __init__(self, name):
    #    #Car.__init__(self, name)
    #    super(SUV, self).__init__(name)
    #    print "SUV object created..."
    pass    

s = SUV("Toyota")


