def enqueue(l, p, e):
    l.setdefault(p, []).append(e)
    print(l)


def dequeue(l):
    if not l:
        print("Queue is empty!")
        return None
    else:
        l = str(l.pop(list(l.keys())[0]))
        l = l[:-2]
        l = l[2:]
        return str(l)


x = {}
enqueue(x, 1, "Monday")
enqueue(x, 2, "Tuesday")
enqueue(x, 3, "Wednesday")
enqueue(x, 4, "Thursday")
enqueue(x, 5, "Friday")
enqueue(x, 7, "Sunday")
enqueue(x, 6, "Saturday")


print("Monday" == dequeue(x))

n = dequeue(x)
print(n)
m = "Tuesday"
print(m)

"""
print(dequeue(x))
print(x)
print(dequeue(x))
print(x)
print(dequeue(x))
print(x)
print(dequeue(x))
print(x)
print(dequeue(x))
print(x)
print(dequeue(x))
print(x)
print(dequeue(x))
"""


"""if __name__ == "__main__":
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
    assert x == {}"""
