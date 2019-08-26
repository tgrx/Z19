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
    #e = [4000, 3000, 2000]
    #e += [1000]

f = open('/Users/alex/Documents/python/2.txt', 'w')
#f.write(a)
f.close()
# print(f.read())
