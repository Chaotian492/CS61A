def rational_1(n, d):
    def select(name):
        if name == "n":
            return n
        elif name == "d":
            return d

    return select


# 分子
def numer(x):
    return x("n")


# 分母
def denom(x):
    return x("d")
