class Car:
    def __init__(self, name):
        print "Car object created: name =", name
        self.name = name

    def __enter__(self):
        print "Entered car context..."
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print "Exited car context..."
        print "exc_type:", exc_type
        print "exc_value:", exc_value
        print "traceback:", traceback


    def __del__(self):
        print "Car object {} destroyed.".format(self.name)


#c = Car("Honda")
#with c:

with Car("Honda") as c:
    print "Using car object:", c.name
    #3 / 0
    print "-------------------"

print "Out of with clause..."


