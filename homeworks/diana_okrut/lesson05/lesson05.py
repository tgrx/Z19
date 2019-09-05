from datetime import date as d, timedelta as t


def Reversed(l):
    if not isinstance(l, (str, tuple, list)):
        return "Введенные данные не соответствуют условию."
    new_l = []
    count = 0
    for i in l:
        x = l[count]
        new_l.insert(0, x)
        count += 1
    return new_l


def Sorted(sample):
    if not sample:
        return sample
    nsample = list(sample)
    left = 0
    right = len(nsample) - 1
    while left <= right:
        for i in range(left, right, +1):
            if nsample[i] > nsample[i + 1]:
                nsample[i], nsample[i + 1] = nsample[i + 1], nsample[i]
        right -= 1

        for i in range(right, left, -1):
            if nsample[i - 1] > nsample[i]:
                nsample[i], nsample[i - 1] = nsample[i - 1], nsample[i]
        left += 1
    return nsample


def Filter(foo, coll):
    r = []
    for c in coll:
        if foo(c):
            r.append(c)
    return r


def TypedReversed(l):
    if not isinstance(l, (str, tuple, list)):
        return "Введенные данные не соответствуют условию."
    new_l = []
    count = 0
    for i in l:
        x = l[count]
        new_l.insert(0, x)
        count += 1
    if type(l) is str:
        return "".join(new_l)
    elif type(l) is tuple:
        return tuple(new_l)
    else:
        return new_l


def LazyReversed(l):
    if not isinstance(l, (str, tuple, list)):
        return "Введенные данные не соответствуют условию."
    new_l = []
    count = 0
    for i in l:
        x = l[count]
        new_l.insert(0, x)
        count += 1
    if type(l) is str:
        a = "".join(new_l)
        return iter(a)
    elif type(l) is tuple:
        a = tuple(new_l)
        return iter(a)
    else:
        return iter(new_l)


# class Range:
#     def __init__(self, stop):
#         self.start = self.current = 0
#         self.stop = stop
#
#     def __iter__(self):
#         self.current = self.start
#         return self
#
#     def __next__(self):
#         if self.current >= self.stop:
#             raise StopIteration
#         c, self.current = self.current, self.current + 1
#         return c
#
#
# def DateRange(tomorrow, next_week):
#     today = d.today()
#     tomorrow = today + t(days=1)
#     next_week = today + t(days=7)
