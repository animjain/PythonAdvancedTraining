import time

class StaffItertor:
    def __init__(self, staff):
        self.staff = staff
        self.i = 0
        self.length = len(self.staff)

    def __next__(self):
        if self.i < self.length:
            m = self.staff._Staff__members[self.i]
            self.i = self.i + 1
            return m
        else:
            raise StopIteration



class Staff:
    def __init__(self, *args):
        self.__members = list(args)
        print("members : ", self.__members)

    def __str__(self):
        return f"staff : {', '.join(self.__members)}"

    def __iter__(self):
        return StaffItertor(self)

    def __len__(self):
        return len(self.__members)


s = Staff("AJ", "TJ", "asdkfj")
print(s)

print("-----------------")


for m in s:
    print(m)