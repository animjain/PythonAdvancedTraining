class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("Created car object", self.name)

    def __enter__(self):
        print("Entered context...")
        if self.name == "Toyota":
            class SUV(Car): pass
            s = SUV(self.name, self.color)
            return s
        else:
            return self

    def drive(self):
        print("Driving", self.name, "priced", self.price, "color:", self.color)

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context....")
        print("exc_type =", exc_type)
        print("exc_value =", exc_value)
        print("traceback =", traceback)

    def __del__(self):
        print("Car object", self.name, "destroyed")


c = Car("Toyota", "red")
print("created car...", c)
with c as s:
    print("Inside with clause...", s)

print("End of program")
