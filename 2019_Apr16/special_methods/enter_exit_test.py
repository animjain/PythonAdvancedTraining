class MyClass:
    def __init__(self):
        print("__init__ called!")
        self.in_context = False

    def __enter__(self):
        print("__enter__ called!")
        self.in_context = True
        return self

    def __exit__(self, et, ev, tb):
        print("__exit__ called!")
        self.in_context = False

if __name__ == '__main__':
    m = MyClass()

    print("m.in_context =", m.in_context)
    with m as a:
        print("In with clause: a =", a)
        print("m.in_context =", m.in_context)
    print("m.in_context =", m.in_context)


