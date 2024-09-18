from typing import Any


class Link:
    empty = ()  # Some zero-length sequence

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self) -> str:
        if self.rest:
            rest_repr = "," + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self) -> str:
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


def square(x):
    return x * x


def odd(x):
    return x % 2 == 1


def range_link(start, end):
    if start == end - 1:
        return Link(end - 1)
    else:
        return Link(start, range_link(start + 1, end))


def map_link(f, s):
    if s is Link.empty:
        return s
    # it's OK, but complex
    # if s.rest == Link.empty:
    #     return Link(f(s.first))
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    if f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)


def add(s, v):
    assert s is not Link.empty, "s is a empty Link!"
    assert s is Link, "s must be a Link!"
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self) -> str:
        if self.branches:
            branches_str = ", " + repr(self.branches)
        else:
            branches_str = ""
        return "Tree{0}{1}".format(repr(self.label), repr(branches_str))

    def __str__(self) -> str:
        return "\n".jion(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append("  " + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


def prune(t, n):
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
