from threading import Thread
from time import sleep

class Counter(Thread):
    def __init__(self, *args, count, **kwargs):
        #Thread.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.count = count

    def run(self):
        for i in range(self.count):
            print(f"{self.name} counting {i}")
            sleep(1)

if __name__ == '__main__':
    t1 = Counter(name="task-a", count=10)
    t2 = Counter(name="task-b", count=20)
    t1.start()

    t2.daemon = True
    t2.start()