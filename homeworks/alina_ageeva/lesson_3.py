def A(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return A(m - 1, 1)
    if m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))
    else:
        return 0


def lenList():
    l = [1]
    try:
        while l:
            l.append(1)
    except MemoryError:
        return len(l)


def lenDict():
    d = {1: 1}
    c = 2
    try:
        while d:
            d.setdefault(c, []).append(1)
            c += 1
    except MemoryError:
        return len(d)


def lenSet():
    s = {1}
    c = 2
    try:
        while s:
            s.add(c)
            c += 1
    except MemoryError:
        return len(s)


def lenStr():
    s = "1"
    try:
        while s:
            s += 1
    except MemoryError:
        return len(s)


def lenTuple():
    t = (1,)
    try:
        while t:
            t += 1
    except MemoryError:
        return len(t)


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


def enqueue(l, p, e):
    l.setdefault(p, []).append(e)


def dequeue(l):
    for p in reversed(sorted(l)):
        a = l[p]
        if not a:
            del l[p]
            continue
        return a.pop(0)


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
