

def fn_cache(fn):
    fn_dict = {}

    def wrap(* args, ** kwargs):
        if args not in fn_dict:
            ret = fn(* args, ** kwargs)
            fn_dict[args] = ret
        else:
            ret = fn_dict[args]
        return ret
    return wrap


@fn_cache
def fetch_web_page(url):
    from urllib.request import urlopen
    response = urlopen(url)
    return response.code


@fn_cache
def square(x):
    from time import sleep
    print("square called: x =", x)
    sleep(2)
    return x*x


print(square(2))
print(square(2))
print(square(2))
