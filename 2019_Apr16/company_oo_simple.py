class Company:
    def __init__(self):
        self.__staff = set()

    def hire(self, m):
        self.__staff.add(m)

    def fire(self, m):
        self.__staff.remove(m)

    def show(self):
        print(", ".join(self.__staff))

    @staticmethod
    def count():
        print("This is a counter...")

