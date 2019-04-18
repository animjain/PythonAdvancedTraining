def buy(): print "The global buy function..."

class Car:
    color = "red"

    def __init__(self, name, price=None):
        self.name = name 
        self.price = price

    def __str__(self): return "Car object: " + self.name

    def __nonzero__(self): return bool(self.price)

    def __len__(self): return 100

    @staticmethod
    def sell():
        print "Car sold..."

    def buy(self): 
        print "bought a car"

    def drive(self):
        print "Driving car: ", self.name
        Car.buy(self) # same as self.buy()
        Car.count()

    @classmethod
    def count(cls):
        print "Count method got first argument: ", cls
        cls.sell()

c1 = Car("Toyota", 35345345345)

if c1: 
    print "c1 is True"
else:
    print "c1 is False"

print len(c1)



