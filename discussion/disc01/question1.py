def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(90, True)
    True
    """

    if temp > 60 and raining == False:
        return False
    else:
        return True


def wears_jacket(temp, raining):
    return temp < 60 or raining
