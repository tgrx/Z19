import timeit

log = open("log.txt", "w")


def fix1():
    x = 100


def fix2():
    x = 100 * 200


def fix3():
    a = 500
    b = 100
    if a >= b:
        return a
    if b >= a:
        return b


def fix4():
    L = list("abc")
    L.append("d")
    L.extend("ehj")
    return L


def fix5():
    K = list("bbac")
    K.remove("b")
    K.remove("b")
    return K


def fix6():
    M = [1, 2, 3, 4, 7, 6, 5, 0, 9, 8]
    if M.index(2):
        return 2
    else:
        return ("Error")


def fix7():
    x = [1, 2, 3, 4, 7, 6, 5, 0, 9, 8]
    x.sort()
    return (x)


result = timeit.timeit("fix2()", setup="from __main__ import fix2")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix3()", setup="from __main__ import fix3")
log.write("SpeedTest3:")
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

result = timeit.timeit("fix6()", setup="from __main__ import fix6")
log.write("SpeedTest6:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix7()", setup="from __main__ import fix7")
log.write("SpeedTest7:")
log.write(str(result))
log.write("\n")
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



