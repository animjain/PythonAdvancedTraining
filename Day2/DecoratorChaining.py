def add_italics(fn):
    def wrapper(*args, **kwargs):
        return "<italics>" + fn(*args, **kwargs) + "</italics>"
    return wrapper

@add_italics
def greet():
    return "hello world"

print(greet())