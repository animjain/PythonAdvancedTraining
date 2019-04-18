attrs = {}

class Car:
    def __init__(self, name, price):
        attrs[id(self)] = {}
        attrs[id(self)]['name'] = name
        attrs[id(self)]['price'] = price

    def drive(self):
        print("Driving", self.name)

    def __getattr__(self, attr):
        if attr == "price":
            raise AttributeError("Invalid access to 'price'")
        return attrs[id(self)][attr]

    def __setattr__(self, attr, value):
        attrs[id(self)][attr] = value

