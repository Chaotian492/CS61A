# import platform

# print("系统", platform.system())

# import time


def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade_short(n):
    print(n)
    if n > 10:
        cascade_short(n // 10)
        print(n)


# T1 = time.time()


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


# T2 = time.time()
# print("程序运行时间：%s毫秒" % ((T2 - T1) * 1000))
def inverse_cascade(n):
    """Print an inverse cascade of prefixes of n.
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


# 使用了lambda和递归，0在python中是个假值
grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


def grow_func(n):
    if n // 10 == 0:
        # base line
        return
    else:
        grow_func(n // 10)
        print(n // 10)


def shrink_func(n):
    if n // 10 == 0:
        # base line
        return
    else:
        print(n // 10)
        shrink_func(n // 10)
