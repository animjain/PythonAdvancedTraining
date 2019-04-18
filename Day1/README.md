from itertools import zip_longest as zip
    > to merge two list and iterate over a and b in single loop as (a[0], b[0]), (a[1], b[1]), (c[1], d[1]), ...


chained itertatoin:
===================
iterate over multiple lists in a single loop and do not create a new collection

    from itertools import chained...


for dictionaries:
=================
from collections import ChainMap
for k,v in ChainMap(r1.headers, r2.header).items



Infinite loop in pyton:
=======================
While true
from itertools import count

for i in count()
  print(i)
  i +=1



 Cycle within limit:
 ===========================
 from itertools import cycle

 for v in cycle(a)
   print(v)




repeat which will print the same value again and again
========================================================
for v in repeat("yes")
  print v


Lambda Function:
================
sqr = lambda x: x*x

a = [1,2,3,4]
list( map(lambda x: x*x*x, a) )
[ x*x*x for x in a ]



Custom modification to a value in list: (say add 50 to list)
======================================
def add(x,y):
  return x+y

 from functools import partial
 addfn = partial(add, 50)               // one value is hard coded
 addfn(10)                  // output 60

 a = [10, 20, 30, 40]
 list(map(addfn, a))



 similarly:
 [ 50+x for x in a ]





 divisible by 3 only:
 ====================
 list(filter(lambda x: x%3 == 0, a))

 [x for x in a if x%3 == 0]





say store square of x if x is divisible by 3:
=============================================
[x*x for x in a if x%3 == 0]

( int(n) for n in numerator.split('/') )


x ** 2      === power to 2
x ** 0.5    === sqr root



merge two dictionaries
=====================
c = dict(a.items() | b.items())

// py-3.6
c = dic(**a, **b)               // keys should be unique




=========================