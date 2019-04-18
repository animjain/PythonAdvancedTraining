class Car:

    @classmethod
    def drive(cls, name):
        print "Driving car", cls, name


#Car.drive("Honda")

c1 = Car()
c1.drive("Toyota")

