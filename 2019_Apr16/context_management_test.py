class SillyLogger:
    def __init__(self, filename):
        print("__init__ invoked...")
        self.filename = filename

    def __enter__(self):
        print("__enter__ invoked...")
        self.logfile = open(self.filename, "a")
        return self

    def log(self, message):
        from time import ctime
        print(f"{ctime()}:{message}", file=self.logfile)

    def __exit__(self, et, ev, tb):
        print(f"__exit__ invoked: {et}, {ev}, {tb}")
        self.logfile.close()

