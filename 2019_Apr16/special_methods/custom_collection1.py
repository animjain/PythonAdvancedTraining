class MyCollection:
    def __init__(self, *args):
        self.__store = dict(enumerate(args))

    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError(f"Invalid index {i}")
        return self.__store.get(i)

    def __len__(self):
        return len(self.__store)

    def __reversed__(self):
        class MyCollectionReversedIterator:
            def __init__(self, iterable):
                self.iterable = iterable
                self.i = len(iterable) - 1

            def __iter__(self): return self

            def __next__(self):
                v = self.iterable[self.i]
                if self.i < 0:
                    raise StopIteration()
                self.i -= 1
                return v

        return MyCollectionReversedIterator(self)
