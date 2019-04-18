class MyCollection:
    def __init__(self, *args):
        self.__collection = list(args)

    def __getitem__(self, i):
       if i > len(self.__collection):
            return None
        else:
            return self.__collection[i]

    def __setitem__(self, i, v):
        if i > len(self.__collection):
            return None
        else:
            self.__collection[i] = v