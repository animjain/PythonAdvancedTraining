class Accumulate:
    def __init__(self, v=0):
        self.value = v

    def __call__(self, v=None):
        if v: self.value += v
        return self.value

a = Accumulate(10)
print a(20)
print a(30)
print a(40)
print a(100)

print "Final result: ", a()

"""

   int a(int v) {
        static value = 0;

        value += v;
        return v;
   }
"""


