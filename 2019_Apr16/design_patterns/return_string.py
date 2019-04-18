def to_upper(fn):
    def wrapper():
        return fn().upper()
    return wrapper


def greet():
    return "Hello world"

print(greet())

greet = to_upper(greet)

def welcome():
    return "Welcome to Python"

welcome = to_upper(welcome)

print(greet())
print(greet())
print(welcome())
print(welcome())

