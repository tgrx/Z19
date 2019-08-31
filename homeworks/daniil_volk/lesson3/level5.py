def enqueue(l, e):
    l.append(e)
    print(l)


def dequeue(l):
    if l:
        return l.pop(0)
    elif l == []:
        print("Queue is empty!")
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
