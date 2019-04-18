class Fibonacci:

    class Iterator:
        def __init__(self, iterable):
            self.fibo = iterable
            self.a, self.b = 0, 1

        def __next__(self):
            v = self.a
            self.a, self.b = self.b, self.a + self.b
            return v

    def __iter__(self):
        return Fibonacci.Iterator(self)


if __name__ == '__main__':
    f = Fibonacci()

    for i in f:
        print(i)



