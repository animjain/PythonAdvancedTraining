class User(type):
    role = "guest"
    pass

# now user class is a metaclass.

Admin = User('Admin', (), {})

a = Admin()
print(a.role)   # this will not work as Admin do not inherit