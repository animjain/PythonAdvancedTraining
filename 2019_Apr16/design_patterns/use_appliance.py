from appliance import *

l = LightBulb()
f = Fan()

a1 = Appliance(l)
a2 = Appliance(f)

a1.price = 100

print a1, a2
print "-" * 20
a1.power_on()
a2.power_on()

