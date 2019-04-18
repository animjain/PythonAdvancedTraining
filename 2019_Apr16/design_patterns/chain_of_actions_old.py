tests = []

def add_test(f):
    tests.append(f)
    return f

@add_test
def add(x, y): return x+y

@add_test
def mul(x, y): return x*y

@add_test
def sub(x, y): return x-y

@add_test
def mul_square(x, y): return x*x * y*y

@add_test
def power_of(x, y): return x ** y

@add_test
def mul_cube(x, y): return x ** 3 * y ** 3

def apply_action(*args, **kwargs):
    for test in tests:
        print("Applying test: {}({})".format(test.__name__, args))
        ret = test(*args, **kwargs)
        print("Result =", ret)
        print("=" * 40)

a = 10
b = 20

apply_action(a, b)
