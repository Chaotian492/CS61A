def index(keys, values, match):
    """
    Return a dictionary from keys k to a list of values
    v for which match(k, v) is a true value.

    >>> index([7, 8, 9], range(30, 50), lambda k, v:v % k == 0)
    {7:[35, 42, 49], 9:[36, 45], 11:[33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
