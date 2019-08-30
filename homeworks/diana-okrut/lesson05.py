from datetime import date as d, timedelta as t


def Reversed(l):
    '''функция возвращает список из элементов коллекции-аргумента, но которые в обратном порядке'''
    types = (str, tuple, list)
    if type(l) not in types:
        print('Введенные данные не соответствуют условию.')
    else:
        new_l = []
        count = 0
        for i in l:
            x = l[count]
            new_l.insert(0, x)
            count += 1
        return new_l


# def Sorted(x):
#     '''функция возвращает список из элементов коллекции-аргумента, которые отсортированы по возрастанию'''
#     new_x = []
#     a = None
#     for i in x:
#         a = i
#         if x[0] <= i:
#             new_x.append(i)
#     return new_x


def Filter(foo, coll):
    '''функция возвращает список (r) из элементов коллекции-аргумента, для которых предикат истинен'''
    r = []
    for c in coll:
        if foo(c):
            r.append(c)
    return r


def TypedReversed(l):
    '''функция возвращает коллекцию того же типа, который имеет аргумент, но в обратном порядке'''
    types = (str, tuple, list)
    if type(l) not in types:
        print('Введенные данные не соответствуют условию.')
    else:
        new_l = []
        count = 0
        for i in l:
            x = l[count]
            new_l.insert(0, x)
            count += 1
        if type(l) is str:
            return ''.join(new_l)
        elif type(l) is tuple:
            return tuple(new_l)
        else:
            return new_l


def LazyReversed(l):
    '''функция возвращает итератор коллекции того же типа, который имеет аргумент, но в обратном порядке'''
    types = (str, tuple, list)
    if type(l) not in types:
        print('Введенные данные не соответствуют условию.')
    else:
        new_l = []
        count = 0
        for i in l:
            x = l[count]
            new_l.insert(0, x)
            count += 1
        if type(l) is str:
            a = ''.join(new_l)
            return iter(a)
        elif type(l) is tuple:
            a = tuple(new_l)
            return iter(a)
        else:
            return iter(new_l)

class Range:
    def __init__(self, stop):
        self.start = self.current = 0
        self.stop = stop
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        c, self.current = self.current, self.current + 1
        return c


# def DateRange(tomorrow,next_week):
#     today = d.today()
#     tomorrow = today + t(days=1)
#     next_week = today + t(days=7)
