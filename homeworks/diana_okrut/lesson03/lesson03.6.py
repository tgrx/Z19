def enqueue(l, p, e):
    l.setdefault(p, []).append(e)


def dequeue(l):
    for p in sorted(l):
        q = l[p]
        if not q:
            del l[p]
            continue
        return q.pop(0)


if __name__ == "__main__":
    x = {}
    assert dequeue(x) is None
    assert enqueue(x, 1, "a") is None
    assert enqueue(x, 1, "b") is None
    assert enqueue(x, 2, "aa") is None
    assert dequeue(x) == "a"
    assert enqueue(x, 1, "c") is None
    assert enqueue(x, 3, "aaa") is None
    assert enqueue(x, 3, "bbb") is None
    assert enqueue(x, 2, "bb") is None
    assert dequeue(x) == "b"
    assert dequeue(x) == "c"
    assert dequeue(x) == "aa"
    assert dequeue(x) == "bb"
    assert dequeue(x) == "aaa"
    assert dequeue(x) == "bbb"
    assert dequeue(x) is None
    assert x == {}
