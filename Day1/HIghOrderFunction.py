def apply(function, list):
    result = []

    for value in list:
        result.append( function(value) )

    return result


def sqaure(x): return x*x

l = [10, 20, 30]
re = apply(sqaure, l)

print(re)