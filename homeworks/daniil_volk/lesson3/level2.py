import timeit
results = open('results.txt', 'w')


def test1():
    x = 100500


def test2():
    x = 100*100/100


def test3():
    100 == 500


def test4():
    volk = ['v','o','l']+['k']


def test5():
    ['v','o', 'l', 'k'].remove('k')


def test6():
    ('volk').index("o")


def test7():
    sorted((3,2,1))

result = timeit.timeit("test1()", setup="from __main__ import test1", number=1000)
results.write("Operation: x = 100500.")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")

result = timeit.timeit("test2()", setup="from __main__ import test2", number=1000)
results.write("Operation: x = 100*100/100.")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")

result = timeit.timeit("test3()", setup="from __main__ import test3", number=1000)
results.write("Operation: 100 == 500.")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")

result = timeit.timeit("test4()", setup="from __main__ import test4", number=1000)
results.write("Operation: list1 += ['k'].")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")

result = timeit.timeit("test5()", setup="from __main__ import test5", number=1000)
results.write("Operation: ['v','o', 'l', 'k'].remove('k').")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")

result = timeit.timeit("test6()", setup="from __main__ import test6", number=1000)
results.write("Operation: ('volk').index('o')")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")

result = timeit.timeit("test7()", setup="from __main__ import test7", number=1000)
results.write("Operation: sorted((3,2,1)).")
results.write(" Time for 1000 loops: ")
results.write(str(result))
results.write("\n")
