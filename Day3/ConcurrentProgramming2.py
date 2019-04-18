from time import sleep
from collections import deque

def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        yield
        sleep(0.5)

def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        yield
        sleep(0.5)

if __name__ == '__main__':
    t1 = foo()
    t2 = bar()
    tasks = deque([t1, t2])
    while tasks:
        t = tasks[0]
        try:
            next(t)
        except StopIteration:
            tasks.popleft()
        else:
            tasks.rotate(-1)