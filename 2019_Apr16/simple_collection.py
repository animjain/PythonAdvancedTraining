# coding: utf-8
class Square:
    def __init__(self, limit):
        self.__limit = limit
    def __getitem__(self, i):
        if i < self.__limit:
            return i*i
        else:
            raise IndexError(f"{i}")
    def __len__(self):
        return self.__limit
    def __contains__(self, v):
        return v < (self.__limit ** 2)
    
