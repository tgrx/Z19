def enqueue(l, e):
    """ добавляет элемент в конец очереди """
    l.append(e)


def dequeue(l):
    """
   вынимает элемент из начала очереди и возвращает его
   если очередь пуста - возвращается None
   """
    if not l:
        return None
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
