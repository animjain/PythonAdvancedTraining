def to_upper(f):
    def wrapper(*args,**kwargs):
        r = f(*args, **kwargs)
        return r.upper()
    return wrapper

@to_upper
def greet(user):
    return "hello " +  user

@to_upper
def welcome(name, city):
    return "Hello {}, welcome to {}".format(name, city)


print(greet("john"))
print(welcome("sam", "pune"))

