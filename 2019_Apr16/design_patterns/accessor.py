class Car:
    def __init__(self):
        print("Car object created..")

    def __getattr__(self, attr):
        print "Getting", attr, "of car..."
        if attr == "sell":
            def sell():
                print "Car is sold..."
            return sell
        else:
            return "not implemented"

    def __setattr__(self, attr, value):
        print "Setting", attr, "to", value

    def drive(self):
        print("Driving car...")

c = Car()

print c.name

c.sell()

c.name = "Honda"
c.price = 10000000
c.color = "white"
