import math
from datetime import date as d, timedelta as t


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
            if r[z] > r[z + 1]:
                t = r[z]
                r[z] = r[z + 1]
                r[z + 1] = t
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



a = datetime.datetime.today()
numdays = 100
dateList = []
for x in range (0, numdays):
    dateList.append(a - datetime.timedelta(days = x))
print "dateList"
