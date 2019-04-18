class Company():

    def __init__(self, *members):
        staff = set(members)

        def hire(s):
            staff.add(s)

        def fire(s):
            staff.remove(s)

        def __str__():
            return "Company(" + str(list(staff)) + ")"

        self.employ, self.terminate, self.__str__ = hire, fire, __str__



if __name__ == '__main__':
    my_startup = Company("Smith", "Sam", "Jones")

    print(my_startup)

    my_startup.hire("Jane")
    my_startup.hire("Bourne")

    my_startup.fire("Smith")

    print(my_startup)



