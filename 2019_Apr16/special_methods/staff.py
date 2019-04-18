class Staff:
    def __init__(self, *args):
        self.members = args

    def __iter__(self):
        class StaffIterator:
            def __init__(self, staff):
                self.staff = staff
                self.staff_len = len(staff.members)
                self.i = 0

            def __next__(self):
                if self.i >= self.staff_len:
                    raise StopIteration
                v = self.i
                self.i += 1
                return self.staff.members[v]

        def __reversed__(self):
            class StaffReverseIterator:
                def __init__(self, staff):
                    self.staff = staff
                    self.i = len(staff.members)

                def __next__(self):
                    if self.i <=  0:
                        raise StopIteration
                    v = self.i
                    self.i - 1
                    return self.staff.members[v]

            return StaffIterator(self)

    def __len__(self):
        return len(self.members)



