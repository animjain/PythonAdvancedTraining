a = [10, 20, 30, 40]

# for v in a: print(a)

iterator = iter(a)
if hasattr(a, '__len__'):
    length = len(a)
    while length:
        v = next(iterator)
        # body of 'for' loop
        print(v)
        length -= 1
else:
    try:
        while True:
            v = next(iterator)
            # body of 'for' loop
            print(v)
    except StopIteration:
        pass

