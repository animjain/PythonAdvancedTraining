class User:
    def __init__(self):
        print("User object created...")

    def __del__(self):
        print("User object is being destroyed...")

u1 = User()
print("u1 =", u1)
u2 = u1
print("u2 =", u2)
del u1
print("u1 deleted...")
print("u2 =", u2)
u2 = 100
print("u2 =", u2)
