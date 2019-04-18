class Car:
    instance_count = 0

    @classmethod
    def increment(cls):
        cls.instance_count += 1

    def __init__(self):
        #self.__class__.instance_count += 1
        self.increment()

    @classmethod
    def test(o):
        print("o =", o)

    @staticmethod
    def drive():
        print("Driving car...")


c = Car()
c.test()
Car.test()

# Car.test(Car)
