import timeit
from decimal import Decimal


decim1 = Decimal("0.33")
decim2 = Decimal("1.66")
s = "ab" * 10000 + "c"
L = [i for i in range(10000)]
T = tuple(i for i in range(10000))
S = {i for i in range(10000)}
D = {i: i for i in range(10000)}
R = range(10000)
results = open("results.txt", "w")


def test1_1():
    return 5 ** 7 + 7 ** 5


def test1_2():
    return 17 ** 19 + 19 ** 17


def test1_3():
    return 1e30 + 1e-30


def test1_4():
    return 1 + 2j + 2 - 1j


def test1_5():
    return decim1 + decim2


def test1_6():
    return Decimal(5 ** 7 + 7 ** 5)


def test1_7():
    return Decimal(17 ** 19 + 19 ** 17)


def test2_1():
    return 5 ** 7 * 7 ** 5


def test2_2():
    return 17 ** 19 * 19 ** 17


def test2_3():
    return 1e30 * 1e-30


def test2_4():
    return 1 + 2j * 2 - 1j


def test2_5():
    return decim1 * decim2


def test2_6():
    return Decimal(5 ** 7 * 7 ** 5)


def test2_7():
    return Decimal(17 ** 19 * 19 ** 17)


def test3_1():
    return 5 ** 7 / 7 ** 5


def test3_2():
    return 17 ** 19 / 19 ** 17


def test3_3():
    return 1e30 / 1e-30


def test3_4():
    return 1 + 2j / 2 - 1j


def test3_5():
    return decim1 / decim2


def test3_6():
    return Decimal(5 ** 7 / 7 ** 5)


def test3_7():
    return Decimal(17 ** 19 / 19 ** 17)


def test4_1():
    return "a" in s


def test4_2():
    return "b" in s


def test4_3():
    return "c" in s


def test4_4():
    return "ab" in s


def test4_5():
    return "ba" in s


def test4_6():
    return "bc" in s


def test4_7():
    return "ac" in s


def test4_8():
    return "ababababababababababc" in s


def test5_1_1():
    return 0 in L


def test5_1_2():
    return 9999 in L


def test5_1_3():
    return 10000 in L


def test5_2_1():
    return 0 in T


def test5_2_2():
    return 9999 in T


def test5_2_3():
    return 10000 in T


def test5_3_1():
    return 0 in S


def test5_3_2():
    return 9999 in S


def test5_3_3():
    return 10000 in S


def test5_4_1():
    return 0 in D


def test5_4_2():
    return 9999 in D


def test5_4_3():
    return 10000 in D


def test5_5_1():
    return 0 in R


def test5_5_2():
    return 9999 in R


def test5_5_3():
    return 10000 in R


result1_1 = timeit.timeit(
    "test1_1()", setup="from __main__ import test1_1", number=1000
)
results.write("Test: для int: 5**7 + 7**5 ")
results.write(" Time for 1000 loops: ")
results.write(str(result1_1))
results.write("\n")


result1_2 = timeit.timeit(
    "test1_2()", setup="from __main__ import test1_2", number=1000
)
results.write("Test: для int: 17**19 + 19**17 ")
results.write(" Time for 1000 loops: ")
results.write(str(result1_2))
results.write("\n")


result1_3 = timeit.timeit(
    "test1_3()", setup="from __main__ import test1_3", number=1000
)
results.write("Test: для float: 1e30 + 1e-30 ")
results.write(" Time for 1000 loops: ")
results.write(str(result1_3))
results.write("\n")


result1_4 = timeit.timeit(
    "test1_4()", setup="from __main__ import test1_4", number=1000
)
results.write("Test: для complex: 1+2j + 2-1j ")
results.write(" Time for 1000 loops: ")
results.write(str(result1_4))
results.write("\n")


result1_5 = timeit.timeit(
    "test1_5()", setup="from __main__ import test1_5", number=1000
)
results.write('Test: для Decimal: "0.33" + "1.66" ')
results.write(" Time for 1000 loops: ")
results.write(str(result1_5))
results.write("\n")


result1_6 = timeit.timeit(
    "test1_6()", setup="from __main__ import test1_6", number=1000
)
results.write("Test: для Decimal: 5**7 + 7**5 ")
results.write(" Time for 1000 loops: ")
results.write(str(result1_6))
results.write("\n")


result1_7 = timeit.timeit(
    "test1_7()", setup="from __main__ import test1_7", number=1000
)
results.write("Test: для Decimal: 17**19 + 19**17 ")
results.write(" Time for 1000 loops: ")
results.write(str(result1_7))
results.write("\n\n")


result2_1 = timeit.timeit(
    "test2_1()", setup="from __main__ import test2_1", number=1000
)
results.write("Test: для int: 5**7 * 7**5 ")
results.write(" Time for 1000 loops: ")
results.write(str(result2_1))
results.write("\n")


result2_2 = timeit.timeit(
    "test2_2()", setup="from __main__ import test2_2", number=1000
)
results.write("Test: для int: 17**19 * 19**17 ")
results.write(" Time for 1000 loops: ")
results.write(str(result2_2))
results.write("\n")


result2_3 = timeit.timeit(
    "test2_3()", setup="from __main__ import test2_3", number=1000
)
results.write("Test: для float: 1e30 * 1e-30 ")
results.write(" Time for 1000 loops: ")
results.write(str(result2_3))
results.write("\n")


result2_4 = timeit.timeit(
    "test2_4()", setup="from __main__ import test2_4", number=1000
)
results.write("Test: для complex: 1+2j * 2-1j ")
results.write(" Time for 1000 loops: ")
results.write(str(result2_4))
results.write("\n")


result2_5 = timeit.timeit(
    "test2_5()", setup="from __main__ import test2_5", number=1000
)
results.write('Test: для Decimal: "0.33" * "1.66" ')
results.write(" Time for 1000 loops: ")
results.write(str(result2_5))
results.write("\n")


result2_6 = timeit.timeit(
    "test2_6()", setup="from __main__ import test2_6", number=1000
)
results.write("Test: для Decimal: 5**7 * 7**5 ")
results.write(" Time for 1000 loops: ")
results.write(str(result2_6))
results.write("\n")


result2_7 = timeit.timeit(
    "test2_7()", setup="from __main__ import test2_7", number=1000
)
results.write("Test: для Decimal: 17**19 * 19**17 ")
results.write(" Time for 1000 loops: ")
results.write(str(result2_7))
results.write("\n\n")


result3_1 = timeit.timeit(
    "test3_1()", setup="from __main__ import test3_1", number=1000
)
results.write("Test: для int: 5**7 / 7**5 ")
results.write(" Time for 1000 loops: ")
results.write(str(result3_1))
results.write("\n")


result3_2 = timeit.timeit(
    "test3_2()", setup="from __main__ import test3_2", number=1000
)
results.write("Test: для int: 17**19 / 19**17 ")
results.write(" Time for 1000 loops: ")
results.write(str(result3_2))
results.write("\n")


result3_3 = timeit.timeit(
    "test3_3()", setup="from __main__ import test3_3", number=1000
)
results.write("Test: для float: 1e30 / 1e-30 ")
results.write(" Time for 1000 loops: ")
results.write(str(result3_3))
results.write("\n")


result3_4 = timeit.timeit(
    "test3_4()", setup="from __main__ import test3_4", number=1000
)
results.write("Test: для complex: 1+2j / 2-1j ")
results.write(" Time for 1000 loops: ")
results.write(str(result3_4))
results.write("\n")


result3_5 = timeit.timeit(
    "test3_5()", setup="from __main__ import test3_5", number=1000
)
results.write('Test: для Decimal: "0.33" / "1.66" ')
results.write(" Time for 1000 loops: ")
results.write(str(result3_5))
results.write("\n")


result3_6 = timeit.timeit(
    "test3_6()", setup="from __main__ import test3_6", number=1000
)
results.write("Test: для Decimal: 5**7 / 7**5 ")
results.write(" Time for 1000 loops: ")
results.write(str(result3_6))
results.write("\n")


result3_7 = timeit.timeit(
    "test3_7()", setup="from __main__ import test3_7", number=1000
)
results.write("Test: для Decimal: 17**19 / 19**17 ")
results.write(" Time for 1000 loops: ")
results.write(str(result3_7))
results.write("\n\n")


result4_1 = timeit.timeit(
    "test4_1()", setup="from __main__ import test4_1", number=1000
)
results.write('Test: "a" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_1))
results.write("\n")


result4_2 = timeit.timeit(
    "test4_2()", setup="from __main__ import test4_2", number=1000
)
results.write('Test: "b" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_2))
results.write("\n")


result4_3 = timeit.timeit(
    "test4_3()", setup="from __main__ import test4_3", number=1000
)
results.write('Test: "c" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_3))
results.write("\n")


result4_4 = timeit.timeit(
    "test4_4()", setup="from __main__ import test4_4", number=1000
)
results.write('Test: "ab" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_4))
results.write("\n")


result4_5 = timeit.timeit(
    "test4_5()", setup="from __main__ import test4_5", number=1000
)
results.write('Test: "ba" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_5))
results.write("\n")


result4_6 = timeit.timeit(
    "test4_6()", setup="from __main__ import test4_6", number=1000
)
results.write('Test: "bc" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_6))
results.write("\n")


result4_7 = timeit.timeit(
    "test4_7()", setup="from __main__ import test4_7", number=1000
)
results.write('Test: "ac" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_7))
results.write("\n")


result4_8 = timeit.timeit(
    "test4_8()", setup="from __main__ import test4_8", number=1000
)
results.write('Test: "ababababababababababc" in s = "ab" * 10000 + "c" ')
results.write(" Time for 1000 loops: ")
results.write(str(result4_8))
results.write("\n\n")


result5_1_1 = timeit.timeit(
    "test5_1_1()", setup="from __main__ import test5_1_1", number=1000
)
results.write("Test: 0 in [i for i in range(10000)] ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_1_1))
results.write("\n")


result5_1_2 = timeit.timeit(
    "test5_1_2()", setup="from __main__ import test5_1_2", number=1000
)
results.write("Test: 9999 in [i for i in range(10000)] ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_1_2))
results.write("\n")


result5_1_3 = timeit.timeit(
    "test5_1_3()", setup="from __main__ import test5_1_3", number=1000
)
results.write("Test: 10000 in [i for i in range(10000)] ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_1_3))
results.write("\n\n")


result5_2_1 = timeit.timeit(
    "test5_2_1()", setup="from __main__ import test5_2_1", number=1000
)
results.write("Test: 0 in tuple(i for i in range(10000)) ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_2_1))
results.write("\n")


result5_2_2 = timeit.timeit(
    "test5_2_2()", setup="from __main__ import test5_2_2", number=1000
)
results.write("Test: 9999 in tuple(i for i in range(10000)) ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_2_2))
results.write("\n")


result5_2_3 = timeit.timeit(
    "test5_2_3()", setup="from __main__ import test5_2_3", number=1000
)
results.write("Test: 10000 in tuple(i for i in range(10000)) ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_2_3))
results.write("\n\n")


result5_3_1 = timeit.timeit(
    "test5_3_1()", setup="from __main__ import test5_3_1", number=1000
)
results.write("Test: 0 in {i for i in range(10000)} ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_3_1))
results.write("\n")


result5_3_2 = timeit.timeit(
    "test5_3_2()", setup="from __main__ import test5_3_2", number=1000
)
results.write("Test: 9999 in {i for i in range(10000)} ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_3_2))
results.write("\n")


result5_3_3 = timeit.timeit(
    "test5_3_3()", setup="from __main__ import test5_3_3", number=1000
)
results.write("Test: 10000 in {i for i in range(10000)} ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_3_3))
results.write("\n\n")


result5_4_1 = timeit.timeit(
    "test5_4_1()", setup="from __main__ import test5_4_1", number=1000
)
results.write("Test: 0 in {i:i for i in range(10000)} ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_4_1))
results.write("\n")


result5_4_2 = timeit.timeit(
    "test5_4_2()", setup="from __main__ import test5_4_2", number=1000
)
results.write("Test: 9999 in {i:i for i in range(10000)} ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_4_2))
results.write("\n")


result5_4_3 = timeit.timeit(
    "test5_4_3()", setup="from __main__ import test5_4_3", number=1000
)
results.write("Test: 10000 in {i:i for i in range(10000)} ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_4_3))
results.write("\n\n")


result5_5_1 = timeit.timeit(
    "test5_5_1()", setup="from __main__ import test5_5_1", number=1000
)
results.write("Test: 0 in range(10000) ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_5_1))
results.write("\n")


result5_5_2 = timeit.timeit(
    "test5_5_2()", setup="from __main__ import test5_5_2", number=1000
)
results.write("Test: 9999 in range(10000) ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_5_2))
results.write("\n")


result5_5_3 = timeit.timeit(
    "test5_5_3()", setup="from __main__ import test5_5_3", number=1000
)
results.write("Test: 10000 in range(10000) ")
results.write(" Time for 1000 loops: ")
results.write(str(result5_5_3))
results.write("\n")
results.write("\n")


results.write(
    "____________________________________LEVEL 3____________________________________"
)
results.write("\n\n")


percents = 100 - ((result1_1 / result1_6) * 100)
results.write(
    str(
        "int: 5**7 + 7**5 faster than Decimal: 5**7 и 7**5  for "
        + str(percents)
        + " percents"
    )
)
results.write("\n")

percents = 100 - ((result1_2 / result1_7) * 100)
results.write(
    str(
        "int: 17**19 + 19**17 faster than Decimal: 17**19 + 19**17  for "
        + str(percents)
        + " percents"
    )
)
results.write("\n\n")

percents = 100 - ((result2_1 / result2_6) * 100)
results.write(
    str(
        "int: 5**7 * 7**5 faster than Decimal: 5**7 * 7**5  for "
        + str(percents)
        + " percents"
    )
)
results.write("\n")

percents = 100 - ((result2_2 / result2_7) * 100)
results.write(
    str(
        "int: 17**19 * 19**17 faster than Decimal: 17**19 * 19**17  for "
        + str(percents)
        + " percents"
    )
)
results.write("\n\n")

percents = 100 - ((result3_1 / result3_6) * 100)
results.write(
    str(
        "int: 5**7 / 7**5 faster than Decimal: 5**7 / 7**5  for "
        + str(percents)
        + " percents"
    )
)
results.write("\n")

percents = 100 - ((result3_2 / result3_7) * 100)
results.write(
    str(
        "int: 17**19 / 19**17 faster than Decimal: 17**19 / 19**17  for "
        + str(percents)
        + " percents"
    )
)
results.write("\n\n")


test1 = {}
test1.setdefault(int(result5_1_1 * 1000000), ["list  "])
test1.setdefault(int(result5_2_1 * 1000000), ["tuple "])
test1.setdefault(int(result5_3_1 * 1000000), ["set   "])
test1.setdefault(int(result5_4_1 * 1000000), ["dict  "])
test1.setdefault(int(result5_5_1 * 1000000), ["range "])


test2 = {}
test2.setdefault(int(result5_1_2 * 1000000), ["list  "])
test2.setdefault(int(result5_2_2 * 1000000), ["tuple "])
test2.setdefault(int(result5_3_2 * 1000000), ["set   "])
test2.setdefault(int(result5_4_2 * 1000000), ["dict  "])
test2.setdefault(int(result5_5_2 * 1000000), ["range "])


test3 = {}
test3.setdefault(int(result5_1_3 * 1000000), ["list  "])
test3.setdefault(int(result5_2_3 * 1000000), ["tuple "])
test3.setdefault(int(result5_3_3 * 1000000), ["set   "])
test3.setdefault(int(result5_4_3 * 1000000), ["dict  "])
test3.setdefault(int(result5_5_3 * 1000000), ["range "])


results.write(
    "Below written has the format: \n "
    "the first line is the slowest type, his speed accepted as one; \n"
    "another lines are the faster types, their speed shows how many times they are faster the slowest type.\n\n"
)


results.write("\nTime for searching 0: \n")
slowest = list(reversed(sorted(test1.keys())))
slowest = slowest[0]


for p in reversed(sorted(test1)):
    results.write(str(str(test1[p]) + str(slowest / p)))
    results.write("\n")


results.write("\nTime for searching 9999: \n")
slowest = list(reversed(sorted(test2.keys())))
slowest = slowest[0]


for p in reversed(sorted(test2)):
    results.write(str(str(test2[p]) + str(slowest / p)))
    results.write("\n")


results.write("\nTime for searching 10000: \n")
slowest = list(reversed(sorted(test3.keys())))
slowest = slowest[0]


for p in reversed(sorted(test3)):
    results.write(str(str(test3[p]) + str(slowest / p)))
    results.write("\n")
