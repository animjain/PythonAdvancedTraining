from person import Person

class Employee(Person):

    def __init__(self, name="Joe"):
        super(classobj).__init__(self, name)
        #Person.__init__(self, name)
        print "Employe init method called, self=", self
     

