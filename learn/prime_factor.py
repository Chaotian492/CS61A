def prime_factor_v1(n):
    """Print the prime factor of n.

    >>> prime_factor(8)
    2
    2
    2
    >>> prime_factor(9)
    3
    3
    >>> prime_factor(15)
    3
    5
    >>> prime_factor(11)
    11
    >>> prime_factor(12)
    2
    2
    3
    >>> prime_factor(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)


def smallest_prime_factor(n):
    """Return the smallest k > 1 that evently divides n."""

    k = 2
    while n % k != 0:
        k = k + 1
    return k


def prime_factor_v2(n):
    k = n
    while n > 1:
        for i in range(2, k // 2, 1):
            if n % i == 0:
                print(i)
                break
        n = n // i


def prime_factor_v3(n):
    while n > 1:
        smallest_prime = 2
        while n % smallest_prime != 0:
            smallest_prime = smallest_prime + 1
        n = n // smallest_prime
        print(smallest_prime)


prime_factor_v2(4324)
# factor2(8)
