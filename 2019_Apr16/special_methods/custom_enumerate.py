class Enumerate:
    def __init__(self, iterable):
        self.i = 0
        self.iterable = iterable

    def __iter__(self): return self

    def __next__(self):
        if self.i >= len(self.iterable):
            raise StopIteration

        rec = self.i, self.iterable[self.i]
        self.i += 1
        return rec