
class ObjectPool:

    def __init__(self, capacity, *args, **kwargs):
        from queue import Queue
        self.pool = Queue(capacity)
        self.capacity = capacity
        self.args = args
        self.kwargs = kwargs

    def __call__(self, cls):
        class Adapter:
            def __init__(s, *args, **kwargs):
                s.__obj = self.pool.get()
                s.__obj.__init__(*args, **kwargs)

            def __getattr__(s, attr):
                return getattr(s.__obj, attr)

            def __setattr__(s, attr, val):
                return setattr(s._obj, attr, val)

            def __delattr__(s, attr):
                return delattr(s, attr)
        Adapter.__name__ = cls.__name__ + "Pool[{}]".format(self.capacity)
        for i in range(self.capacity):
            self.pool.put(cls(*self.args, **self.kwargs))
        return Adapter


@ObjectPool(5)
class Foo:
    def __init__(self):
        print("Foo object created: ", id(self))



if __name__ == '__main__':
    store = {}
    for i in range(10):
        store[i] = Foo()

    for k, v in store.items(): print(k, v)

