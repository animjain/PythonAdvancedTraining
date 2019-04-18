class Accumulator:
    def __init__(self, val):
        self.val = val

    def __call__(self, val=None):
        if not val: 
            return self.val
        else:
            self.val += val


