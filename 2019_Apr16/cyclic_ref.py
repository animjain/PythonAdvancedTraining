from __future__ import print_function

class Person:
    def __init__(self):
        print("Person object created...")

    def __del__(self):
        print("Person object destroyed...")

class Car:
    def __init__(self):
        print("Car object created...")

    def __del__(self):
        print("Car object destroyed...")


p = Person()
c = Car()
p.owns = c
c.owner = p
