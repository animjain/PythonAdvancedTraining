class Car(type):
    def __new__(cls):
        print "__new__() called with first argument: ", cls
        return type.__new__(cls, None)
        
    def __init__(self):
        print "__init__() called with first argument: ", self


c = Car()


