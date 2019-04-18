


def decorate_module_functions(module, decorator):
    from types import FunctionType
    for attr in dir(module):
        if type(getattr(module, attr)) is FunctionType:
            setattr(module, attr, decorator(getattr(module, attr)))


if __name__ == '__main__':
    import simple_test_functions

    def log(fn):
        def wrapper():
            with open("functions.log", "a") as logfile:
                ret = fn()
                logfile.write("{}() returned {}.\n".format(fn.__qualname__, ret))
            return ret
        return wrapper


    def to_upper(fn):
        def wrapper():
            return fn().upper()
        return wrapper

    decorate_module_functions(simple_test_functions, log)

    print(simple_test_functions.greet())
    print(simple_test_functions.test())
    print(simple_test_functions.welcome())
