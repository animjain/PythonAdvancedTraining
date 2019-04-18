class ElectronicDevice:

    def poweron(e):
        print(e.name, "powered on")

    def poweroff(e):
        print(e.name, "powered off")

    def buy(self):
        print("Bought an electronic device")
        print("Got an object belonging to ", self.__class__)

