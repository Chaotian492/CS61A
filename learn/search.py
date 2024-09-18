def search(f):
    """找到一个最小的非负值让f(x)的返回值为真，然后返回这个值
    f -- a function
    """
    x = 0
    # while True:  # 无限循环
    #     if f(x):  # 判断f(x)的返回值
    #         return x
    #     x += 1

    while not f(x):
        x += 1
    return x


def is_three(x):
    """if x==3 -> return true else return false."""
    return x == 3


def square(x):
    return x * x


def positive(x):
    """if x*x-100>0 -> return true else return false."""
    return max(0, square(x) - 100)


def inverse(f):
    """Return a function g(y) that returns x such that f(x) == y.
    >>> sqrt=inverse(square)
    >>> sqrt(16)
    4
    """

    def inverse_of_f(y):
        def is_inverse_of_y(x):
            return f(x) == y

        return search(is_inverse_of_y)

    return inverse_of_f
    # return lambda y: search(lambda x: f(x) == y)
