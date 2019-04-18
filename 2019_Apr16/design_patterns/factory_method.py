def buy(x):
    if x == "car": 
        def vehicle():
            print "Driving car..."
    elif x == "bike":
        def vehicle():
            print "Riding bike..."
    elif x == "plane":
        def vehicle():
            print "Flying a plane..."
    else:
        def vehicle():
            print "Bought nothing useful"

    return vehicle


v = buy("plane")
v()

v1 = buy("car")
v1()

v2 = buy("bike")
v2()


