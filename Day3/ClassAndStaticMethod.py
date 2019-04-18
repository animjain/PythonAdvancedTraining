class User:

    @staticmethod
    def testfn(a, b):
        print(f"in testfn,   a = {a}  and b = {b}")

    @classmethod
    def testfnn(a, b):
        print(f"in testfnn,   a = {a}  and b = {b}")

u = User()
u.testfn(10, 20)

u.testfnn(10)

# u.testfnn(10,20)     >> Unexpected argument error now as it is a class method