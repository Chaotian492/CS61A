def f_list(s=[]):
    # append adds one element to a list, the element can be a list.
    # and them have same address.
    s.append(5)
    return len(s)


# def f_couple(s=()):
#     # couple has no attribute append

#     s.append(5)
#     return len(s)


def f():
    s = []
    b = [1, 23, 4]

    # adds all element in one list to another list.
    s.extend(b)
    print(s)
    # return s
    a = s + [[5, 0]]

    # slice create a new list
    b = a[1:]
    a[3][1] = 1

    # list function can create a new list.
    # new list and old list contain same elements,but their address are different.
    k = list(a)
    k[1] = 222
    k[3][1] = 9

    # slice assignment replaces a slice with new values.
    k[0:0] = [4554, 32]
    print(a, b, k)


def k():
    s, t = [2, 3], [5, 6]
    # pop remove and return the last element
    t = s.pop()
    print(s, t)

    t = [5, 6]
    # remove the first element equal to the argument
    t.remove(5)
    print(t)
    print(f"this is list t= {t}.")

    # remove element by slice assignment.
    t[0:1] = []
    print(t)


def g():
    t = [[1, 2], [3, 4]]
    t[0].append(t[1:2])
    s = []
    s.append(t[1:2])
    print(f"t: {t}, s: {s}, t[1:2]: {t[1:2]}")
