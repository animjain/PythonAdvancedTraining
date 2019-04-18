class Counter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        class CounterIterator:
            def __init__(self, counter):
                self.counter = counter
                self.i = 0

            def __next__(self):
                if self.i > self.counter.n:
                    raise StopIteration
                v = self.i
                self.i += 1
                return v

        return CounterIterator(self)



