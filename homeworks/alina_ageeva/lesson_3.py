m = int(input("Введите число m > 0\t"))
n = int(input("Введите число n > 0\t"))


def Ackerman(m, n):
    stack = []
    while True:
        if not m:
            if not stack:
                return n + 1
            m, n = stack.pop(), n + 1
        elif not n:
            m, n = m - 1, 1
        else:
            stack.append(m - 1)
            n -= 1


print(Ackerman(m, n))


def lenList():
    l = [1]
    try:
        while l:
            l.append(1)
    except MemoryError:
        return len(l)


# 156_097_847


def lenDict():
    d = {1: 1}
    c = 2
    try:
        while d:
            d.setdefault(c, []).append(1)
            c += 1
    except MemoryError:
        return len(d)


# 19_650_740


def lenSet():
    s = {1}
    c = 2
    try:
        while s:
            s.add(c)
            c += 1
    except MemoryError:
        return len(s)


# 20_132_659


def lenStr():
    s = "1"
    try:
        while s:
            s += 1
    except MemoryError:
        return len(s)


# 268_435_456


def lenTuple():
    t = (1,)
    try:
        while t:
            t += 1
    except MemoryError:
        return len(t)


# 67_108_864


def enqueue(l, e):
    l.append(e)


def dequeue(l):
    if l:
        return l.pop(0)
    if l == []:
        return None


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


def enqueue(l, p, e):
    l = {1: 1}
    p = input()
    e = input()
    l[p] = e
    print(l)


def dequeue(l):
    if l == {}:
        return None
    if l:
        return l[0]


if __name__ == "__main__":
    x = {}
    assert dequeue(x) is None
    assert enqueue(x, 1, "a") is None
    assert enqueue(x, 1, "b") is None
    assert enqueue(x, 2, "aa") is None
    assert dequeue(x) == "aa"
    assert enqueue(x, 1, "c") is None
    assert enqueue(x, 3, "aaa") is None
    assert enqueue(x, 3, "bbb") is None
    assert enqueue(x, 2, "bb") is None
    assert dequeue(x) == "aaa"
    assert dequeue(x) == "bbb"
    assert dequeue(x) == "bb"
    assert dequeue(x) == "a"
    assert dequeue(x) == "b"
    assert dequeue(x) == "c"
    assert dequeue(x) is None
    assert x == {}
