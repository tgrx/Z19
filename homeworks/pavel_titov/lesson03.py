import timeit
from decimal import Decimal as D


log = open("log.txt", "w")


def fix11():
    a = int(5**7)
    b = int(7**5)
    c = int(17**19)
    d = int(19**17)

    z = a+b
    x = c+d

    return z, x

def fix12():
    a = float(1e30)
    b = float(1e-30)
    z = a+b
    return z

def fix13():
    a = complex(1+2j)
    b = complex(2-1j)
    z = a+b
    return z

def fix14():
    a = D(0.33)
    b = D(1.66)
    c = D(5**7)
    d = D(7**5)
    e = D(19**17)
    f = D(17**19)
    z = a+b
    x = c+d
    y = e+f
    return z , x , y


def fix21():
    a = int(5 ** 7)
    b = int(7 ** 5)
    c = int(17 ** 19)
    d = int(19 ** 17)

    z = a * b
    x = c * d

    return z, x


def fix22():
    a = float(1e30)
    b = float(1e-30)
    z = a * b
    return z


def fix23():
    a = complex(1 + 2j)
    b = complex(2 - 1j)
    z = a * b
    return z


def fix24():
    a = D(0.33)
    b = D(1.66)
    c = D(5 ** 7)
    d = D(7 ** 5)
    e = D(19 ** 17)
    f = D(17 ** 19)
    z = a * b
    x = c * d
    y = e * f
    return z, x, y


def fix31():
    a = int(5 ** 7)
    b = int(7 ** 5)
    c = int(17 ** 19)
    d = int(19 ** 17)

    z = a / b
    x = c / d

    return z, x


def fix32():
    a = float(1e30)
    b = float(1e-30)
    z = a / b
    return z


def fix33():
    a = complex(1 + 2j)
    b = complex(2 - 1j)
    z = a / b
    return z


def fix34():
    a = D(0.33)
    b = D(1.66)
    c = D(5 ** 7)
    d = D(7 ** 5)
    e = D(19 ** 17)
    f = D(17 ** 19)
    z = a / b
    x = c / d
    y = e / f
    return z, x, y


def fix4():
    s = "ab" * 10000 + "c"
    for i in s:
        if i == "a":
            return True
        else:
            return False



def fix5(L):
    L = []
    for i in range(10000):
        if i == 0:
            return i
        if i == 9999:
            return 9999
        if i == 10000:
            return 10000




result = timeit.timeit("fix11()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix12()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix13()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix14()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix21()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix22()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix23()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix24()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix31()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix32()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix33()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix34()", setup="from __main__ import fix1")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")



result = timeit.timeit("fix4()", setup="from __main__ import fix4")
log.write("SpeedTest4:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix5()", setup="from __main__ import fix5")
log.write("SpeedTest5:")
log.write(str(result))
log.write("\n")



# Функция Аккермана


def akker(a, b):
    if a == 0:
        return b + 1
    if b == 0:
        return akker(a - 1, 1)
    return akker(a - 1, akker(a, b - 1))

#Уровень 5


def enqueue(l, e):
    l.append(e)



def dequeue(l):
    if l:
        return l.pop(0)

if __name__ == "__main__":
    x = []
    assert dequeue(x) is None
    assert enqueue(x, 1) is None
    assert enqueue(x, 2) is None
    assert dequeue(x) == 1
    assert enqueue(x, 3) is None
    assert dequeue(x) == 2
    assert dequeue(x) == 3
    assert dequeue(x) is None
    assert x == []
#Уровень 6

def enqueue(l, e, p):
    l.setdefault(p, []).append(e) #возвращает значение 2 элемента - з и то что вставлено


def dequeue(l):
    sorted_key = sorted(l)
    order_key = reversed(sorted_key)
    for p in order_key:
        q = l[p]
        if not q:
            del l[p]
        return l.pop(0)



