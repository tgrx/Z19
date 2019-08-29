from datetime import date as d, timedelta as t


def Reversed(l):
    if type(l)is not (list or str or tuple):
        print('Введенные данные не являются неизменяемой коллекцией')
    else:
        l = list(l)
        new_l = []
        n = 0
        for i in l:
            x = l[n]
            new_l.insert(0,x)
            n += 1
        return new_l


def Sorted(x):
    x = list(x)
    new_x = []
    for i in x:
        if x[0] < i:
            new_x.append(i)
    return new_x
#
# def Filter(foo, coll):
#     l = []
#     for c in coll:
#         if foo(c):
#             l.append(c)
#
#
#
# def DateRange(tomorrow,next_week):
#     today = d.today()
#     tomorrow = today + t(days=1)
#     next_week = today + t(days=7)
