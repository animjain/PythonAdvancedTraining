
class Fibonacci:
    def __init__(self, max):
        self.max = max

    class Iterator:
        def __init__(self, iterable):
            self.fibo = iterable
            self.a, self.b = 0, 1
            self.i = 0

        def next(self):
            if self.i >= self.fibo.max:
                raise StopIteration

            v = self.a
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return v

    def __iter__(self):
        return Fibonacci.Iterator(self)


if __name__ == '__main__':
    f = Fibonacci(10)

    for i in f:
        print i,

