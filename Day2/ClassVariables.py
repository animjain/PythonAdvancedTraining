import sys
print(sys.version)

class car:
    window = 4

class SUV(car):
    pass

# c is instanceof car but it inherits base class

c = car()
print(c.window)

b = car()
b.window = 5

print(c.window)
print(b.window)

print(c.__class__)     # every object is of type type
print()       # if it inherits from a class, that class name otw object


print("=================")
s = SUV()
print(s.__class__)     # every object is of type type
print(SUV.__bases__)       # if it inherits from a class, that class name otw object

print("=================")
print(isinstance(s,c.__class__))
print(isinstance(s,car))

