class Person:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print self.name, "says 'Hello'"

p = Person("john")

p()

