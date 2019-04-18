class Person(object):

    def __init__(self, name="Guest"):
        print "Person init method called, self=", self
        self.name = name


    def greet(self):
        print self.name, "says Hello"

