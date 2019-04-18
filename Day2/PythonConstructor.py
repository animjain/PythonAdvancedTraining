"""
This is factory pattern. Depending upon the input, we are creating the objects
"""
import sys
print(sys.getrecursionlimit())

class Admin: pass
class Guest: pass

class User:
    def __new__(cls, name, *args, **kwargs):
        if(name == "root"):
            return Admin()
        elif(name == "guest"):
            return Guest()
        else:
            """
            same as for function here ^^^

            we are creating object of super class so passed cls to new as argument and then we are calling new of super just like
            we are doing for User.__new__
            """
            return super().__new__(cls)
            # return User() ----> this will stuck in infitnie loop of new of User.

    """
    init will be called only when we are creating the object of User.
    """
    def __init__(self, name):
        print("init invoked...")


u = User("root")
print(u)
print("====================")
x = User("animesh")
print(x)