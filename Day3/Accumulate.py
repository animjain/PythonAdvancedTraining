def accumulate():
    print("inside accumulate ")
    total = 0
    while True:
        v = yield                               # waiting for send to be called...
        if v is None:
            break
        total += v
        yield total                             # next(a) will get this value now...
    return total

print("calling accumlate now")
a = accumulate()
print("called accumlate now")

next(a)             # since a is generator
print("next called now")


print(a.send(10))
next(a)

print(a.send(20))
next(a)

try:
    print(a.send(None))
except StopIteration:
    pass
