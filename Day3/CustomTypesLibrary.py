from time import sleep

class RunQueue:
    def __init__(self):
        from collections import deque
        self.rq = deque()

    def add(self, fn, *args, **kwargs):
        from types import GeneratorType
        task = fn(*args, **kwargs)
        if type(task) is not GeneratorType:
            raise TypeError(f"function {fn.__qualname__} does not yield!")
        else:
            self.rq.append(task)

    def schedule(self):
        while self.rq:
            task = self.rq[0]
            try:
                next(task)
            except StopIteration:
                self.rq.popleft()
            else:
                self.rq.rotate(-1)