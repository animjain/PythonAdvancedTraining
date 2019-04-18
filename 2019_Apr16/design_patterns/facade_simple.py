class Car:

    def __dir__(self):
        return self.__dict__.keys()

    def __getattr__(self, attr):
        def buy():
            print "Buying car"

        def sell():
            print "Sold car"

        def not_implemented():
            print "Not implemented"

        if attr == 'sell':
           return sell
        elif attr == 'buy':
            return buy
        else:
            return not_implemented

