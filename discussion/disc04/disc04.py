def count_stair_ways(n):
    assert n > 0, "n must be positive number."
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for i in range(1, k + 1):
            total += count_k(n - i, k)
        return total


def even_weighted(s):
    return [a * s[a] for a in range(len(s)) if a % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))
