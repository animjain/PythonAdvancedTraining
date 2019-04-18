def to_upper(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

class ToUpper:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs).upper()

@ToUpper  # greet = ToUpper(greet)
#@to_upper
def greet():
    return "Hello world"

print(greet())


@to_upper
def welcome():
    return "Welcome to Python"



print(greet())
print(greet())
print(welcome())
print(welcome())

