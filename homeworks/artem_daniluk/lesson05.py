def Reversed(coll):
    coll = list(coll)
    rev_coll = []
    for i in range(len(coll) - 1, -1, -1):
        rev_coll.append(coll[i])
    return rev_coll


def Sorted(col):
    r = list(col)
    for i in range(len(col) - 1):
        for j in range(len(col) - i - 1):
            if r[j] > r[j + 1]:
                t = r[j]
                r[j] = r[j + 1]
                r[j + 1] = t
    return r


def Filter(p, col):
    col = list(col)
    r = []
    for i in range(len(col)):
        if p(col[i]):
            r.append(col[i])
    return r


def TypedReversed(coll):
    t = type(coll)
    coll = list(coll)
    rev_coll = []
    for i in range(len(coll) - 1, -1, -1):
        rev_coll.append(coll[i])
    if t == str:
        rev_coll = "".join(rev_coll)
    else:
        rev_coll = t(rev_coll)
    return rev_coll


def LazyReversed(coll):
    coll = list(coll)
    rev_coll = []
    for i in range(len(coll) - 1, -1, -1):
        rev_coll.append(coll[i])
    return iter(rev_coll)


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
