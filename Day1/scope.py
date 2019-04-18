color = "white"

class Car:
    color = "red"

    def __init__(self):
        self.color = "blue"

    def myColor(self):
        # here color is not defined in function scope and not used with self, so global color will be used.
        print("color is ", color)

    def selfColor(self):
        print("self color is : ", self.color)


c = Car()


# Global object
c.myColor()

# instance object
c.selfColor()

# static object
print(Car.color)