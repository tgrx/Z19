# Lesson 5
# from datetime import date, timedelta
# Уровень 2


def Reversed(Obj):
    if len(Obj) == 0:
        return None
    spisok = []
    ind = len(Obj)
    while ind:
        ind -= 1
        spisok += [Obj[ind]]
    return spisok


# Уровень 3


def Sorted(Coll):
    Coll = list(Coll)
    for j in range(len(Coll) - 1):
        for i in range(len(Coll) - j - 1):
            if Coll[i] > Coll[i + 1]:
                Coll[i], Coll[i + 1] = Coll[i + 1], Coll[i]
    print(Coll)


# Уровень 4

# def Filter(x, y):
#     y = list(y)
#     new = []
#     for i in range(len(y)):
#         if x is y[i]:
#             new.append(x)
#     return new

# Уровень 5


def TypedReversed(Str):
    t = type(Str)
    if len(Str) == 0:
        return None
    spisok = []
    ind = len(Str)
    while ind:
        ind -= 1
        spisok += [Str[ind]]
    a = t(spisok)
    return a


# Уровень 6

# def LazyReversed(Str):
#     for i in reversed(Str):
#         print(i)
#
# # Уровень 7
#
# def Range(first, last, step = 1):
#     while first < last:
#         print(first)
#         first+= step
#
# # def Range_1(number):
# #     i = 0
# #     while i != number:
# #         print(i)
# #         i+=1
#
# # Уровень 8
# # Получилось только так:
#
# def DateRange(first_date, last_date):
#     for i in range(int((last_date - first_date).days)):
#         yield (first_date + timedelta(i))
#
# first_date = date.today()
# nextweek = first_date + timedelta(days=7)
# last_date = nextweek
# for day in DateRange(first_date, last_date):
#     print(day.strftime("%d-%m-%Y"))
