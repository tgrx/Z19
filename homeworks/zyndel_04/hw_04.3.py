def lenList():
    lst = [1]
    try:
        while lst:
            lst.append(1)
    except MemoryError:
        return len(lst)
    pass


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
    pass


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
    pass


# 20_132_659


def lenStr():
    s = "1"
    try:
        while s:
            s *= 2
    except MemoryError:
        return len(s)
    pass


# 134_217_728


def lenTuple():
    t = (1,)
    try:
        while t:
            t += t
    except MemoryError:
        return len(t)
    pass


# 33_554_432

# def lenFrozenset():
#    f = frozenset('1')
#   a = 2
#   try:
#       while f:
#          f | frozenset('f"a')
#       a += 1
#   except MemoryError:
#      return len(f)
#  pass

#
