def trace1(fn):
    def traced(x):
        print("calling", fn, "on argument", x)
        return fn(x)

    return traced


@trace1
def square(x):
    return x * x
