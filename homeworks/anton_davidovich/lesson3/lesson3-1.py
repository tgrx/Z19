import timeit

int1 = 5 ** 7
int2 = 7 ** 5


def test1_1():
    """int1 + int2: """
    return int1 + int2


print(test1_1.__doc__)
print(timeit.timeit(test1_1, number=1000))

int3 = 17 ** 19
int4 = 19 ** 17


def test1_2():
    """int3 + int4: """
    return int3 + int4


print(test1_2.__doc__)
print(timeit.timeit(test1_2, number=1000))

int5 = 1e30
int6 = 1e-30


def test1_3():
    """int5 + int6: """
    return int5 + int6


print(test1_3.__doc__)
print(timeit.timeit(test1_3, number=1000))

int7 = 1 + 2j
int8 = 1 - 2j


def test1_4():
    """int7 + int8: """
    return int7 + int8


print(test1_4.__doc__)
print(timeit.timeit(test1_4, number=1000))

int9 = 0.33
int10 = 1.66


def test1_5():
    """int9 + int10: """
    return int9 + int10


print(test1_5.__doc__)
print(timeit.timeit(test1_5, number=1000))

int11 = 5.0 ** 7.0
int12 = 7.0 ** 5.0


def test1_6():
    """int11 + int12: """
    return int11 + int12


print(test1_6.__doc__)
print(timeit.timeit(test1_6, number=1000))

int13 = 17.0 ** 19.0
int14 = 19.0 ** 17.0


def test1_7():
    """int13 + int14: """
    return int13 + int14


print(test1_7.__doc__)
print(timeit.timeit(test1_7, number=1000))

int1 = 5 ** 7
int2 = 7 ** 5


def test2_1():
    """int1 + int2: """
    return int1 * int2


print(test2_1.__doc__)
print(timeit.timeit(test2_1, number=1000))

int3 = 17 ** 19
int4 = 19 ** 17


def test2_2():
    """int3 + int4: """
    return int3 * int4


print(test2_2.__doc__)
print(timeit.timeit(test2_2, number=1000))

int5 = 1e30
int6 = 1e-30


def test2_3():
    """int5 + int6: """
    return int5 * int6


print(test2_3.__doc__)
print(timeit.timeit(test2_3, number=1000))

int7 = 1 + 2j
int8 = 1 - 2j


def test2_4():
    """int7 + int8: """
    return int7 * int8


print(test2_4.__doc__)
print(timeit.timeit(test2_4, number=1000))

int9 = 0.33
int10 = 1.66


def test2_5():
    """int9 + int10: """
    return int9 * int10


print(test2_5.__doc__)
print(timeit.timeit(test2_5, number=1000))

int11 = 5.0 ** 7.0
int12 = 7.0 ** 5.0


def test2_6():
    """int11 + int12: """
    return int11 * int12


print(test2_6.__doc__)
print(timeit.timeit(test2_6, number=1000))

int13 = 17.0 ** 19.0
int14 = 19.0 ** 17.0


def test2_7():
    """int13 + int14: """
    return int13 * int14


print(test2_7.__doc__)
print(timeit.timeit(test2_7, number=1000))

int1 = 5 ** 7
int2 = 7 ** 5


def test3_1():
    """int1 + int2: """
    return int1 / int2


print(test3_1.__doc__)
print(timeit.timeit(test3_1, number=1000))

int3 = 17 ** 19
int4 = 19 ** 17


def test3_2():
    """int3 + int4: """
    return int3 / int4


print(test3_2.__doc__)
print(timeit.timeit(test3_2, number=1000))

int5 = 1e30
int6 = 1e-30


def test3_3():
    """int5 + int6: """
    return int5 / int6


print(test3_3.__doc__)
print(timeit.timeit(test3_3, number=1000))

int7 = 1 + 2j
int8 = 1 - 2j


def test3_4():
    """int7 + int8: """
    return int7 / int8


print(test3_4.__doc__)
print(timeit.timeit(test3_4, number=1000))

int9 = 0.33
int10 = 1.66


def test3_5():
    """int9 + int10: """
    return int9 / int10


print(test3_5.__doc__)
print(timeit.timeit(test3_5, number=1000))

int11 = 5.0 ** 7.0
int12 = 7.0 ** 5.0


def test3_6():
    """int11 + int12: """
    return int11 / int12


print(test3_6.__doc__)
print(timeit.timeit(test3_6, number=1000))

int13 = 17.0 ** 19.0
int14 = 19.0 ** 17.0


def test3_7():
    """int11 + int12: """
    return int13 / int14


print(test3_7.__doc__)
print(timeit.timeit(test3_7, number=1000))

s = "ab" * 10000 + "c"


def test4_1():
    """a" + s: """
    return "a" in s


print(test4_1.__doc__)
print(timeit.timeit(test4_1, number=1000))


def test4_2():
    """b" + s: """
    return "b" in s


print(test4_2.__doc__)
print(timeit.timeit(test4_2, number=1000))


def test4_3():
    """c" + s: """
    return "c" in s


print(test4_3.__doc__)
print(timeit.timeit(test4_3, number=1000))


def test4_4():
    """c" + s: """
    return "c" in s


print(test4_4.__doc__)
print(timeit.timeit(test4_4, number=1000))


def test4_5():
    """ab" + s: """
    return "ab" in s


print(test4_5.__doc__)
print(timeit.timeit(test4_5, number=1000))


def test4_6():
    """ba" + s: """
    return "ba" in s


print(test4_6.__doc__)
print(timeit.timeit(test4_6, number=1000))


def test4_7():
    """bc" + s: """
    return "bc" in s


print(test4_7.__doc__)
print(timeit.timeit(test4_7, number=1000))


def test4_8():
    """ac" + s: """
    return "ac" in s


print(test4_8.__doc__)
print(timeit.timeit(test4_8, number=1000))


def test4_9():
    """"ababababababababababc" + s: """
    return "ababababababababababc" in s


print(test4_9.__doc__)
print(timeit.timeit(test4_8, number=1000))

L = [i for i in range(10000)]


def test5_1():
    """0 + L: """
    return 0 in L


print(test5_1.__doc__)
print(timeit.timeit(test5_1, number=1000))


def test5_2():
    """9999 + L: """
    return 9999 in L


print(test5_2.__doc__)
print(timeit.timeit(test5_2, number=1000))


def test5_3():
    """10000 + L: """
    return 10000 in L


print(test5_3.__doc__)
print(timeit.timeit(test5_3, number=1000))

T = tuple(i for i in range(10000))


def test6_1():
    """0 + T: """
    return 0 in T


print(test6_1.__doc__)
print(timeit.timeit(test6_1, number=1000))


def test6_2():
    """9999 + T: """
    return 9999 in T


print(test6_2.__doc__)
print(timeit.timeit(test6_1, number=1000))


def test6_3():
    """10000 + T: """
    return 10000 in T


print(test6_3.__doc__)
print(timeit.timeit(test6_3, number=1000))

S = {i for i in range(10000)}


def test7_1():
    """0 + S: """
    return 0 in S


print(test7_1.__doc__)
print(timeit.timeit(test7_1, number=1000))


def test7_2():
    """9999 + S: """
    return 9999 in S


print(test7_2.__doc__)
print(timeit.timeit(test7_2, number=1000))


def test7_3():
    """10000 + S: """
    return 10000 in S


print(test7_3.__doc__)
print(timeit.timeit(test7_3, number=1000))
