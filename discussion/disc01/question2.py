def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return True
    k = 2
    while k < n / 2:
        if n % k == 0:
            return False
        k += 1
    return True
