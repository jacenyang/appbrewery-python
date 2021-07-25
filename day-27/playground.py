def add(*args):
    m = 0
    for n in args:
        m += n
    return m


print(add(1, 2, 3, 4))


def calculate(n, **kwargs):
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    return n


print(calculate(2, add=3, multiply=5))
