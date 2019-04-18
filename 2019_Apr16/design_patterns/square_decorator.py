def numeric_args(fn):
    def wrapper(*args):
        new_args = []
        for arg in args:
            try:
                new_args.append(int(arg))
            except Exception as e:
                #raise type(e)("Invalid argument passed - must be a number")
                new_args.append(0)

        return fn(*new_args)
    return wrapper

@numeric_args
def square(x):
    return x*x


print(square([10, 20, 30]))