import math


def Reversed(x):
    x = list(x)
    rev_x = []
    for i in range(len(x) - 1, -1, -1):
        rev_x.append(x[i])
    return rev_x


def Sorted(x):
    r = list(x)
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if r[j] > r[j + 1]:
                t = r[j]
                r[j] = r[j + 1]
                r[j + 1] = t
    return r


def Filter(p, x):
    x = list(x)
    r = []
    for i in range(len(x)):
        if p(x[i]):
            r.append(x[i])
    return r


def TypedReversed(x):
    t = type(x)
    x = list(x)
    rev_x = []
    for i in range(len(x) - 1, -1, -1):
        rev_x.append(x[i])
    if t == str:
        rev_x = "".join(rev_x)
    else:
        rev_x = t(rev_x)
    return rev_x


def LazyReversed(x):
    x = list(x)
    rev_x = []
    for i in range(len(x) - 1, -1, -1):
        rev_x.append(x[i])
    return iter(rev_x)


class Range:
    def __init__(self, *args):
        if not args:
            raise TypeError("Enter stop")
        if len(args) == 2:
            self.step = 1
            self.start = args[0]
            self.stop = args[1]
            self.current = args[0]
        if len(args) == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
            self.current = 0
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
            self.current = args[0]

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.stop >= self.start and self.step < 0:
            raise StopIteration
        if self.stop <= self.start and self.step > 0:
            raise StopIteration
        if self.start < self.stop:
            if self.current >= self.stop:
                raise StopIteration
            c, self.current = self.current, self.current + self.step
            return c
        elif self.start > self.stop:
            if self.current <= self.stop:
                raise StopIteration
            c, self.current = self.current, self.current + self.step
            return c
