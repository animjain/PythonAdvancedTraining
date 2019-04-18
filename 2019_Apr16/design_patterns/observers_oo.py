from collections import defaultdict

class PubSub:
    class DispatchError(Exception):
        pass

    def __init__(self):
        #self.subscribers = {}
        self.subscribers = defaultdict(list)

    def subscribe(self, on):
        def decorate(target):
            #self.subscribers.setdefault(on, []).append(target)
            self.subscribers[on].append(target)
            return target
        return decorate

    def publish(self, on, *args, **kwargs):
        if on not in self.subscribers:
            raise PubSub.DispatchError("invalid chain on dispatch: " + str(on))

        for subscriber in self.subscribers[on]:
            subscriber(*args, **kwargs)
