def decorate(fn):
    print("Decorating ", fn)

    def wrap(*args, **kwargs):
        print("wrap is called for ", fn)
        return fn(*args, **kwargs)

    return wrap

@decorate
def testfn(val):
    print("this is a test function : ", val)

testfn("anim")