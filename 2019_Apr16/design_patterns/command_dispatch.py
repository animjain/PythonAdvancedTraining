class CommandDispatch:
    def __init__(self):
        self.dispatch_map = {}

    def dispatch(self, command=None):
        def decorate(f):
            if command is not None:
                self.dispatch_map[command] = f
        return decorate

    def invalid(self=None):
        print "*** Invalid command encountered!"

    def set_invalid_command(self, target):
        self.invalid = target

    def run(self):
        def decorate(target):
            def wrap(*args, **kwargs):
                while True:
                    command = target(*args, **kwargs)
                    self.dispatch_map.get(command, self.invalid)()
            wrap()
        return decorate


