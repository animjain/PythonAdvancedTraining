def testfn():
    print("One")
    yield 100
    print("200")

# testfn()      // will not work anymore as python as now internally decorated testfn as it has yeild in it and now it is a generator

g = testfn()

print(next(g))

"""
next(g) : raises StopIteration when all the next is done
"""