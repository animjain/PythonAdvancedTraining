def fib(x):
    a, b = 0, 1
    for _ in range(x):
        print(a)
        a, b = b, a + b


if __name__ == '__main__':
    fib(10)
