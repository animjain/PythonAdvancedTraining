class Car:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def drive(self):
        print("Driving", self.name)

    def __getattr__(self, attr):
        print("Get-attr called!")
        return 100
c

