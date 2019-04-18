
from module_utils import decorate_module_functions

if __name__ == '__main__':
    def to_upper(fn):
        def wrapper():
            return fn().upper()
        return wrapper

    decorate_module_functions(to_upper)
    import simple_test_functions

    print(simple_test_functions.greet())
    print(simple_test_functions.test())
    print(simple_test_functions.welcome())
