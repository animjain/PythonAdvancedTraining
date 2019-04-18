from person import Person

class Student(Person): 

    def __init__(self, name="Anonymous", school="AAA Convent"):
        print "Student init method called, self=", self
        Person.__init__(self, name)
        #super(Student, self).__init__(name)

        self.school = school

    def greet(self):
        print "Student's greet method called."
        Person.greet(self)

