import timeit  # импортируем timeit

# Проверяем время выполнения действий при одних и тех же значениях


print("int(2000) - ", timeit.timeit("int(2000)", number=10000), "cек")  # проверяем время выполнения создания
print("str(2000) - ", timeit.timeit("str(2000)", number=10000), "cек")  # проверяем время выполнения создания
print("tuple([2000, 2000, 2000]) - ", timeit.timeit("tuple([2000, 2000, 2000])", number=10000), "cек")
print("complex(2000, 2000) - ", timeit.timeit("complex(2000, 2000)", number=10000), "cек")
print("bool(2000 != 2000) - ", timeit.timeit("bool(2000 != 2000)", number=10000), "cек")
print("bool(2000 < 1000 < 3000) - ", timeit.timeit("bool(2000 < 1000 < 3000)", number=10000), "cек")
print("x=2000**2000 - ", timeit.timeit("x= 2000**2000", number=10000), "cек")  # проверяем время возведения в степень
print("x=2000*2000 - ", timeit.timeit("x= 2000*2000", number=10000), "cек")  # проверяем время выполнения умножения
print("x=2000/2000 - ", timeit.timeit("x= 2000/2000", number=10000), "cек")  # проверяем время выполнения деления
print("x=2000+2000 - ", timeit.timeit("x= 2000+2000", number=10000), "cек")  # проверяем время выполнения сложения
print("x=2000-2000 - ", timeit.timeit("x= 2000-2000", number=10000), "cек")  # проверяем время выполнения вычитания
# e = [4000, 3000, 2000]
# e += [1000]

f = open('/home/evgen/Documents/lesson03.txt', 'w')  # создаем файл
# f.write(a)       # записываем в файл
f.close()  # закрываем файл


def enqueue(l, e):
    """ добавляет элемент в конец очереди """
    x = list([1, 2, 3, 4, 5])
    x.append(e)
    return x


print(enqueue(1, 7))


def dequeue(l):
    """
   вынимает элемент из начала очереди и возвращает его
   если очередь пуста - возвращается None
   """
    x = list([l])
    if not x:
        return None
    else:
        l = x.pop(0)
        return l


print(dequeue(None))
print(dequeue(4))

# if __name__ == "__main__":
#   x = []
#    assert dequeue(x) is None
#   assert enqueue(x, 1) is None
#  assert enqueue(x, 2) is None
#   assert dequeue(x) == 1
#    assert enqueue(x, 3) is None
#    assert dequeue(x) == 2
#   assert dequeue(x) == 3
#    assert dequeue(x) is None
#    assert x == []
