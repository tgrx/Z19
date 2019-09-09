def enqueue(l, p, e):
    """ добавляет элемент e в конец очереди l с приоритетом p """
    l.setdefault(p, []).append(e)


def dequeue(l):
    """
    вынимает элемент из начала очереди и возвращает его
    если очередь пуста - возвращается None
    элементы возвращаются согласно приоритету
    """
    for p in reversed(sorted(l)):
        q = l[p]
        if not q:
            del l[p]
            continue
        return q.pop(0)
    return


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
