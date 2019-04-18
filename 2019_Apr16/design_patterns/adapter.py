class Fan:
    def __init__(self):
        print("Created a Fan object")
        self.v = 0

    def poweron(self):
        print("Powered ON Fan object")

    def poweroff(self):
        print("Powered OFF Fan object")

    def set_speed(self, v):
        print("Setting speed to", v)
        self.v = v


class LightBulb:
    def __init__(self):
        print("Created a LightBulb object")
        self.v = 0

    def poweron(self):
        print("Powered ON LightBulb object")

    def poweroff(self):
        print("Powered OFF LightBulb object")

    def set_brightness(self, v):
        print("Setting brightness to", v)
        self.v = v


class Appliance:
    def __init__(self, appliance):
        self.__dict__['appliance'] = appliance()

    def __setattr__(self, name, value):
        #self.__dict__['appliance'].name = value
        setattr(self.__dict__['appliance'], name, value)

    def __getattr__(self, name):
        # return self.__dict__['appliance'].name
        return getattr(self.__dict__['appliance'], name)

    def __dir__(self):
        return dir(self.__dict__['appliance'])
