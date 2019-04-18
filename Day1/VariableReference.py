import sys

a = "Hello"

print(sys.getrefcount(a))

b = a

print(sys.getrefcount(a))

del b

print(sys.getrefcount(a))
