def foo():
    print('In foo: __name__', __name__)


name = "John"

if __name__ == '__main__':
    foo()
    print(name)
