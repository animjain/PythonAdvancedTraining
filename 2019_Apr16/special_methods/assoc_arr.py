class Array:
    class array_iterator:
        def __init__(self, array):
            self.array = array
            self.keys = array._Array__store.keys()
            self.i = 0
            self.max = len(self.keys)

        def next(self):
            if self.i >= self.max: raise StopIteration
            v = self.array[self.keys[self.i]]
            self.i += 1
            return self.keys[self.i], v

    def __init__(self, data=()):
        self.__store = dict(enumerate(data))

    def __str__(self):
        return "Array(" + str(self.__store) + ")"
    __repr__ = __str__

    def __getitem__(self, index):
        return self.__store.get(index, None)

    def __setitem__(self, index, value):
        self.__store[index] = value

    def __len__(self):
        return len(self.__store)
        #return max(self.__store.keys()) + 1

    def __iter__(self):
        #return self.array_iterator(self)
        return self.__store.iteritems()

    def __add__(self, other):
        arr = Array()
        arr.__store.update(self.__store)
        for k, v in other:
            if k in arr.__store:
                arr.__store[k] = arr.__store[k], v
        return arr

    #def __cmp__(self, other):
    #    return len(self) - len(other)
    
    def __eq__(self, other):
        return self.__store == other.__store


arr1 = Array([33, 44, 55, 66, 77, 88, 4, 5, 6, 7, 8])
arr2 = Array([100, 200, 300, 400, 55, 66, 77, 88, 99, 55, 44])

#arr3 = arr1 + arr2 # arr1.__add__(arr2) ---> Array.__add__(arr1, arr2)
#print arr3

if arr1 == arr2:
    print "Both arrays are equal..."
elif arr1 > arr2:
    print "arr1 is big"
else:
    print "arr2 is big"




