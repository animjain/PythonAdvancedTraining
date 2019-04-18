class Staff:
    def __init__(self, *args):
        self.__members = list(args)

    def __str__(self):
        return f"staff : {', '.join(self.__members)}"

s = Staff("AJ", "TJ", "asdkfj")
print(s)