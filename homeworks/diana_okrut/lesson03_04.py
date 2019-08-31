##### .02 #####
a = {
    "zyndel": "qwerty",
    "master": 123,
    "alexander": "*12qw",
    "artem": 55567,
    "egor": [1, 5, 7],
    "lol": 17,
    "bugaGA": (1, 3, 6),
}
print("bugaGA" in a)
a["egor"].append(4)
print(a)
# %timeit 'bugaGA' in a       # 53.8 ns
# %timeit a['egor'].append(4) #123 ns

b = 48
c = 54
print(b ** c)
print(b > c)
print((b - c) * b)
# %timeit b ** c      # 830 ns
# %timeit b > c       # 67.2 ns
# %timeit (b - c) * b # 135 ns

d = "xyz"
e = "zyx"
print(d == e)
print(d + e)
# %timeit d == e # 73 ns
# %timeit d + e  # 120 ns

f = [1, 4, 5, 8, 66, 1, 35, 778, 952, 4, 3]
print(f[6])
# %timeit f[6]       # 52.4 ns
f.sort()
print(f)
del f[1:8]
print(f)
# %timeit f.sort()   # 127 ns
# %timeit del f[1:8] # 104 ns

g = "HelloMyDearFriend"
i = list(g)
print(i)


# %timeit list(g) # 444 ns

##### .03 #####

def lenList():
    l = [1]
    try:
        while l:
            l.append(1)
    except MemoryError:
        return len(l)


# 76_998_386


def lenDict():
    d = {1: 1}
    a = 2
    try:
        while d:
            d.setdefault(a, []).append(1)
            a += 1
    except MemoryError:
        return len(d)


# 11_184_810


def lenSet():
    s = {1}
    a = 2
    try:
        while s:
            s.add(a)
            a += 1
    except MemoryError:
        return len(s)


# 20_132_659


def lenStr():
    s = "1"
    try:
        while s:
            s *= 2
    except MemoryError:
        return len(s)


# 134_217_728


def lenTuple():
    t = (1,)
    try:
        while t:
            t += t
    except MemoryError:
        return len(t)


# 33_554_432

##### .04 #####

def A(m, n):
    try:
        if m == 0:
            return n + 1
        if m > 0:
            if n == 0:
                return A(m - 1, 1)
            else:
                return A(m - 1, A(m, n - 1))
    except TypeError:
        return "kek"
    except RecursionError:
        return "Maximum recursion depth exceeded in comparison."


# In [87]: A(3, 8)
# Out[87]: 2045

##### 0.5 #####

def enqueue(l, e):
    l.append(e)
    return None


def dequeue(l):
    if l:
        return l.pop(0)
    else:
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


###### .06 #####

def enqueue(l, p, e):
    l[e] = p
    return None


# def dequeue(l):
#     return l.pop()
#
# if __name__ == "__main__":
#     x = {}
#     assert dequeue(x) is None
#     assert enqueue(x, 1, "a") is None
#     assert enqueue(x, 1, "b") is None
#     assert enqueue(x, 2, "aa") is None
#     assert dequeue(x) == "aa"
#     assert enqueue(x, 1, "c") is None
#     assert enqueue(x, 3, "aaa") is None
#     assert enqueue(x, 3, "bbb") is None
#     assert enqueue(x, 2, "bb") is None
#     assert dequeue(x) == "aaa"
#     assert dequeue(x) == "bbb"
#     assert dequeue(x) == "bb"
#     assert dequeue(x) == "a"
#     assert dequeue(x) == "b"
#     assert dequeue(x) == "c"
#     assert dequeue(x) is None
#     assert x == {}
