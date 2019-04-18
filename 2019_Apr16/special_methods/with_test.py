class Car:
    def __init__(self):
        print("__init__ method called!")

    def __enter__(self):
        print("__enter__ method called!")
        self.opened = True
        return self

#    def __exit__(self, exc_type, exc_value, traceback):
#        print("__exit__ method called: exc_type = {}, exc_value = {}, traceback = {}".format(exc_type, exc_value, traceback))
#        self.opened = False

with Car() as c:
    print("Inside with block...")
    print(c.opened)
    exit(0)
    v = 3 / 0
    print("Exiting with block...")

print("Outside with block:", c.opened)




