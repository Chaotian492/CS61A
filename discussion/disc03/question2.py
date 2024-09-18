def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 1:
        return 1 + hailstone(n * 3 + 1)
    else:
        return 1 + hailstone(n // 2)


def merge(n1, n2):
    """Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10


def make_func_repeater(f, x):
    def repeater(i):
        if i == 0:
            return x
        else:
            return f(repeater(i - 1))

    return repeater


def is_prime(n):
    def prime_helper(index):
        if n == index:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return prime_helper(index + 1)

    return prime_helper(2)
