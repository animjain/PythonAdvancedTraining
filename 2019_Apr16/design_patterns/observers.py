notifiers = {}

def observe(on):
    def decorate(target):
        #observers =  notifiers.get(on, set())
        #observers.add(target)
        #notifiers[on] = observers
        notifiers.setdefault(on, set()).add(target)
        return target
    return decorate

def notify(on, *args, **kwargs):
    if on not in notifiers:
        class DispatchError(Exception): pass
        raise DispatchError("invalid chain on dispatch: " + str(on))

    for target in notifiers[on]:
        target(*args, **kwargs)



