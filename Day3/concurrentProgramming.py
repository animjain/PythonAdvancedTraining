from time import sleep

def foo():
    for i in range(5):
        print(f"foo: counting {i}")
        yield

def bar():
    for i in range(5):
        print(f"bar: counting {i}")
        yield

if __name__ == '__main__':
    t1 = foo()
    t2 = bar()
    tasks = [t1, t2]
    print("here")
    while tasks:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                print("removing ", t)
                tasks.remove(t)

    print("============")
    t = bar()
    while(next(t)):
        print(t)