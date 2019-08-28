Coll# Lesson 5
from datetime import date, timedelta
# Уровень 2

def Reversed(Str):
    print(Str[::-1])

# Уровень 3

def Sorted(Coll):
    for j in range(len(Coll) - 1):
        for i in range(len(Coll)- j -1):
            if Coll[i] > Coll[i + 1]:
                Coll[i], Coll[i + 1] = Coll[i + 1], Coll[i]
    print(Coll)

# Уровень 4

name = (1, 2, 3)
def Filter(name):
    number = (1, 4, 2, 5, 3, 6)
    if name in number:
        return True
    else:
        return False

Filter = filter(Filter, name)
for number in Filter:
    print(number)

# Уровень 5

def TypedReversed(Str):
    t = type(Str)
    print(t(list(reversed(Str))))

# Уровень 6

def LazyReversed(Str):
    for i in reversed(Str):
        print(i)

# Уровень 7

def Range(first, last, step = 1):
    while first < last:
        print(first)
        first+= step

# def Range_1(number):
#     i = 0
#     while i != number:
#         print(i)
#         i+=1

# Уровень 8
# Получилось только так:

def DateRange(first_date, last_date):
    for i in range(int((last_date - first_date).days)):
        yield (first_date + timedelta(i))

first_date = date.today()
nextweek = first_date + timedelta(days=7)
last_date = nextweek
for day in DateRange(first_date, last_date):
    print(day.strftime("%d-%m-%Y"))
