import timeit  # импортируем timeit


def sec(s):
    print(s, timeit.timeit(s, number=10000), "cek")


sec("int(200)")

# Проверяем время выполнения действий при одних и тех же значениях
print(
    "int(2000) - ", timeit.timeit("int(2000)", number=10000), "cек"
)  # проверяем время выполнения создания
print(
    "str(2000) - ", timeit.timeit("str(2000)", number=10000), "cек"
)  # проверяем время выполнения создания
print(
    "tuple([2000, 2000, 2000]) - ",
    timeit.timeit("tuple([2000, 2000, 2000])", number=10000),
    "cек",
)
print(
    "complex(2000, 2000) - ", timeit.timeit("complex(2000, 2000)", number=10000), "cек"
)
print("bool(2000 != 2000) - ", timeit.timeit("bool(2000 != 2000)", number=10000), "cек")
print(
    "bool(2000 < 1000 < 3000) - ",
    timeit.timeit("bool(2000 < 1000 < 3000)", number=10000),
    "cек",
)
print(
    "x=2000**2000 - ", timeit.timeit("x= 2000**2000", number=10000), "cек"
)  # проверяем время возведения в степень
print(
    "x=2000*2000 - ", timeit.timeit("x= 2000*2000", number=10000), "cек"
)  # проверяем время выполнения умножения
print(
    "x=2000/2000 - ", timeit.timeit("x= 2000/2000", number=10000), "cек"
)  # проверяем время выполнения деления
print(
    "x=2000+2000 - ", timeit.timeit("x= 2000+2000", number=10000), "cек"
)  # проверяем время выполнения сложения
print(
    "x=2000-2000 - ", timeit.timeit("x= 2000-2000", number=10000), "cек"
)  # проверяем время выполнения вычитания
# e = [4000, 3000, 2000]
# e += [1000]
a = str(sec("int(200)"))
f = open("/Users/alex/Documents/python/2.txt", "w")  # создаем файл
f.write(a)  # записываем в файл
f.close()  # закрываем файл


def ackermann(m, n):
    """функция Аккермана"""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


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


##def enqueue(l, p, e):
    """ добавляет элемент e в конец очереди l с приоритетом p """


##def dequeue(l):
    """
    вынимает элемент из начала очереди и возвращает его
    если очередь пуста - возвращается None
    элементы возвращаются согласно приоритету
    """
# if __name__ == "__main__":
#    x = {}
#    assert dequeue(x) is None
#    assert enqueue(x, 1, "a") is None
#    assert enqueue(x, 1, "b") is None
#    assert enqueue(x, 2, "aa") is None
#    assert dequeue(x) == "aa"
#    assert enqueue(x, 1, "c") is None
#    assert enqueue(x, 3, "aaa") is None
#    assert enqueue(x, 3, "bbb") is None
#    assert enqueue(x, 2, "bb") is None
#    assert dequeue(x) == "aaa"
#    assert dequeue(x) == "bbb"
#    assert dequeue(x) == "bb"
#    assert dequeue(x) == "a"
#    assert dequeue(x) == "b"
#    assert dequeue(x) == "c"
#    assert dequeue(x) is None
#    assert x == {}
