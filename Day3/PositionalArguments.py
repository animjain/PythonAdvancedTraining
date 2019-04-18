def testfn(a, *c, b=20):
    print(a,b,c)

testfn(10)
testfn(10, 50,30,40)
testfn(10, b=40)



def testfnn(*,  a,  b):
    print()