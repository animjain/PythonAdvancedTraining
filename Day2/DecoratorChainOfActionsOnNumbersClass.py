class ChainOfActions:
    def __init(self):
        self.actions = []

    def add(self, fn):
        self.actions.append(fn)
        return fn

    def apply(*args, **kwargs):
        for fn in self.actions:
            print("Applying test: {}({})".format(fn.__name__, args))
            ret = fn(*args, **kwargs)
            print("Result =", ret)
            print("=" * 40)

tests = ChainOfActions()

