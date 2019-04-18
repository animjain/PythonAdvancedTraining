class TinyLogger:
    def __init__(self, log):
        self.logfile = log

    def __enter__(self):
        self.log = open(self.logfile, "a")
        return self

    """
    both __enter__ and __exit__ should be implemented together
    """
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"et={exc_type}, ev={exc_val}, extb={exc_tb}  ")
        self.log.close()
        del self.log

    def write(self, msg):
        from time import ctime
        print(f"{ctime()}: {msg}, file = self.log")


t = TinyLogger("a.log")

with t:                             # enter will be called
    print("inside with block")
    #t.write("logMessageTest")
    t.write("logMessageTest", "deleteme")
    print("Existing with blockk")   # exis is called here


print("Outside with block")