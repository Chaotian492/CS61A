def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def memo(f):
    cache = {}

    def menoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return menoized


def exp(b, n):
    if n == 0:
        return
