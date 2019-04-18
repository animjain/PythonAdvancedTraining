class User:
    def __init__(self):
        print("user object created")

    def __del__(self):
        print("user object is destroyed")

u1 = User()
u2 = u1     # created one more reference of u2
del u1      # deleting only u1
u2 = 100    # now reference to u1 will be zero and user object deleted.

"""
delete method is called before the garbage collection for the object. 
"""