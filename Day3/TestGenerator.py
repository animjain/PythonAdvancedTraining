def bar():
    for i in range(5):
        print(f"bar: counting {i}")
        yield

if __name__ == '__main__':
    t = bar()
    try:
        while(True):
            next(t)
    except StopIteration:
        pass

# see accumulate to get the value from generator using bar().send and bar.next()