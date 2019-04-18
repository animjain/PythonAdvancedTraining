from __future__ import print_function

class User:
    def __init__(self):
        print("User object being created...")

    def __del__(self):
        print("User object being destroyed...")

u1 = User()
print("u1 =", u1)
u2 = u1
print("u2 =", u2)
u3 = u1
print("u3 =", u3)
del u1
print("u1 deleted...")
u2 = "Hello"
print("u2 =", u2)
u3 = 100
print("u3 =", u3)
