def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

hcf(36, 48)

