call_log = {}

def profile_time(fn):
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        ret = fn(*args, **kwargs)
        duration = time() - start
        call_log[fn.__qualname__] = duration
        return ret
    return wrapper

@profile_time
def range_test(n):
    j = 0
    for i in range(n):
        j += i

@profile_time
def list_range_test(n):
    j = 0
    for i in list(range(n)):
        j += i


range_test(10000000)
list_range_test(10000000)

print(call_log)