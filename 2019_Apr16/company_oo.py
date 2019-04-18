class Company:
    def __init__(self):
        staff = set() 

        def hire(m):
            staff.add(m)

        def fire(m):
            staff.remove(m)

        def show():
            print(", ".join(staff))

        self.hire, self.fire, self.show = hire, fire, show




