class ChainOfActions:
    tests = []
    data = []

    def __init__(self, fn):
        print("Adding {} to tests".format(fn.__qualname__))
        self.__class__.tests.append(fn)
        # type(self).append(fn)

    @classmethod
    def add_data(cls, data):
        print("Adding data: ", data)
        cls.data = data

    @classmethod
    def run(cls):
        print("RUNNING TESTS...")
        for data in cls.data:
            print("*" * 40)
            for fn in cls.tests:
                print("Running test: {}{}".format(fn, str(data)))
                try:
                    print(">>>> ", fn(*data))
                except Exception as e:
                    print("FAILED!")
                else:
                    print("SUCCESS")
                print("-" * 40)
