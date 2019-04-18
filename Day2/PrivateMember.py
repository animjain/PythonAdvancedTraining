class Staff:
    def __init__(self, *args):
        """
        :param args:
        __members : will automatically be private, name mangling by python.

        this will be visible inside class methods.
        S._Staff.__members
        """
        self.__members = list(args)

    def show(self):
        print(self.__members)


s = Staff("ani", "mesh")
s.show()
