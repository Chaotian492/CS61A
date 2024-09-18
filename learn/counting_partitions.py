# 使用2分法，将整体分区分割成包含m和不包含m两种情况。
# 确定三种base line


def trace(f):
    def g(n, m):
        print(f.__name__ + "(" + str(n) + ", " + str(m) + ") was called ")
        result = f(n, m)
        print(f.__name__ + "(" + str(n) + ", " + str(m) + ") -> " + str(result))
        return result

    return g


@trace
def count_partitions(n, m):
    """数字分区,利用一个不大于m的数对n进行分区.
    >>> count_partitions(6,4)
    9
    """
    if n == 0:  # 对0分区只有1种情况
        return 1
    elif n < 0:  # 对非正数分区始终是0种情况
        return 0
    elif m == 0:  # 分区数等于零时，分区为0
        return 0
    else:
        # 包含m的分区情况
        with_m = count_partitions(n - m, min(n - m, m))
        # 不包含m的分区情况
        without_m = count_partitions(n, m - 1)
        return with_m + without_m
