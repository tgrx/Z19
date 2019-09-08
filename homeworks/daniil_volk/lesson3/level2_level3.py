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
variable1 = 5 ** 7
variable2 = 7 ** 5
variable3 = 17 ** 19
variable4 = 19 ** 17
variable5 = 1e30
variable6 = 1e-30
variable7 = 1 + 2j
variable8 = 2 - 1j




def test1_1():
    """(5 ** 7) + (7 ** 5) """
    return variable1 + variable2


def test1_2():
    """17**19 + 19**17 """
    return variable3 + variable4


def test1_3():
    """1e30 + 1e-30 """
    return variable5 + variable6


def test1_4():
    """1+2j + 2-1j """
    return variable7 + variable8


def test1_5():
    """0.33" + "1.66 """
    return decim1 + decim2


def test1_6():
    """5**7 + 7**5 """
    return Decimal(variable1 + variable2)


def test1_7():
    """17**19 + 19**17 """
    return Decimal(variable3 + variable4)


def test2_1():
    """(5 ** 7) * (7 ** 5) """
    return variable1 * variable2


def test2_2():
    """17**19 * 19**17"""
    return variable3 * variable4


def test2_3():
    """1e30 * 1e-30 """
    return variable5 * variable6


def test2_4():
    """1+2j * 2-1j """
    return variable7 * variable8


def test2_5():
    """0.33" * "1.66 """
    return decim1 * decim2


def test2_6():
    """5**7 * 7**5 """
    return Decimal(variable1 * variable2)


def test2_7():
    """17**19 * 19**17 """
    return Decimal(variable3 * variable4)


def test3_1():
    """(5 ** 7) / (7 ** 5) """
    return variable1 / variable2


def test3_2():
    """17**19 / 19**17 """
    return variable3 / variable4


def test3_3():
    """1e30 / 1e-30 """
    return variable5 / variable6


def test3_4():
    """1+2j / 2-1j """
    return variable7 / variable8


def test3_5():
    """0.33" / "1.66 """
    return decim1 / decim2


def test3_6():
    """5**7 / 7**5 """
    return Decimal(variable1 / variable2)


def test3_7():
    """17**19 / 19**17 """
    return Decimal(variable3 / variable4)


def test4_1():
    """searching 'a' in s = "ab" * 10000 + "c" """
    return "a" in s


def test4_2():
    """searching 'b' in s = "ab" * 10000 + "c" """
    return "b" in s


def test4_3():
    """searching 'c' in s = "ab" * 10000 + "c" """
    return "c" in s


def test4_4():
    """searching 'ab' in s = "ab" * 10000 + "c" """
    return "ab" in s


def test4_5():
    """searching 'ba' in s = "ab" * 10000 + "c" """
    return "ba" in s


def test4_6():
    """searching 'bc' in s = "ab" * 10000 + "c" """
    return "bc" in s


def test4_7():
    """searching 'ac' in s = "ab" * 10000 + "c" """
    return "ac" in s


def test4_8():
    """searching 'ababababababababababc' in s = "ab" * 10000 + "c" """
    return "ababababababababababc" in s


def test5_1_1():
    """searching 0 in [i for i in range(10000)] """
    return 0 in L


def test5_1_2():
    """searching 9999 in [i for i in range(10000)] """
    return 9999 in L


def test5_1_3():
    """searching 10000 in [i for i in range(10000)] """
    return 10000 in L


def test5_2_1():
    """searching 0 in tuple(i for i in range(10000)) """
    return 0 in T


def test5_2_2():
    """searching 9999 in tuple(i for i in range(10000)) """
    return 9999 in T


def test5_2_3():
    """searching 10000 in tuple(i for i in range(10000)) """
    return 10000 in T


def test5_3_1():
    """searching 0 in {i for i in range(10000)} """
    return 0 in S


def test5_3_2():
    """searching 9999 in {i for i in range(10000)} """
    return 9999 in S


def test5_3_3():
    """searching 10000 in {i for i in range(10000)} """
    return 10000 in S


def test5_4_1():
    """searching 0 in {i:i for i in range(10000)} """
    return 0 in D


def test5_4_2():
    """searching 9999 in {i:i for i in range(10000)} """
    return 9999 in D


def test5_4_3():
    """searching 10000 in {i:i for i in range(10000)}     """
    return 10000 in D


def test5_5_1():
    """searching 0 in range(10000) """
    return 0 in R


def test5_5_2():
    """searching 9999 in range(10000) """
    return 9999 in R


def test5_5_3():
    """searching 10000 in range(10000) """
    return 10000 in R


tests = (test1_1, test1_2, test1_3, test1_4, test1_5, test1_6, test1_7,
         test2_1, test2_2, test2_3, test2_4, test2_5, test2_6, test2_7,
         test3_1, test3_2, test3_3, test3_4, test3_5, test3_6, test3_7,
         test4_1, test4_2, test4_3, test4_4, test4_5, test4_6, test4_7, test4_8,
         test5_1_1, test5_1_2, test5_1_3,
         test5_2_1, test5_2_2, test5_2_3,
         test5_3_1, test5_3_2, test5_3_3,
         test5_4_1, test5_4_2, test5_4_3,
         test5_5_1, test5_5_2, test5_5_3,
         )

results = open("results.txt", "w")





def benchmark(testing, filename):
    filename.write(
            'Function: '
            + str(testing.__doc__)
            + " \n"
            + 'Time: '
            + str(round(timeit.timeit(testing, number = 1000), 5))
            + " \n\n"
        )
    return round(timeit.timeit(testing, number = 1000), 5)



with open("results.txt", "w") as filename:
    for test in tests:
        benchmark(test, filename)

    filename.write(
        "Below written has the format: \n "
        "the first line is the slowest type, his speed accepted as one; \n"
        "another lines are the faster types, their speed shows how many times they are faster the slowest type.\n\n"
    )

    test1 = {
        timeit.timeit(test5_1_1, number = 1000): ["list  "],
        timeit.timeit(test5_2_1, number = 1000): ["tuple "],
        timeit.timeit(test5_3_1, number = 1000): ["set   "],
        timeit.timeit(test5_4_1, number = 1000): ["dict  "],
        timeit.timeit(test5_5_1, number = 1000): ["range "]
    }

    filename.write("\nTime for searching 0: \n")
    slowest = list(reversed(sorted(test1.keys())))
    slowest = slowest[0]

    for p in reversed(sorted(test1)):
        filename.write(str(str(test1[p]) + str(slowest / p)))
        filename.write("\n")

    test2 = {
        timeit.timeit(test5_1_2, number = 1000): ["list  "],
        timeit.timeit(test5_2_2, number = 1000): ["tuple "],
        timeit.timeit(test5_3_2, number = 1000): ["set   "],
        timeit.timeit(test5_4_2, number = 1000): ["dict  "],
        timeit.timeit(test5_5_2, number = 1000): ["range "]
    }

    filename.write("\nTime for searching 9999: \n")
    slowest = list(reversed(sorted(test2.keys())))
    slowest = slowest[0]

    for p in reversed(sorted(test2)):
        filename.write(str(str(test2[p]) + str(slowest / p)))
        filename.write("\n")

    test3 = {
        timeit.timeit(test5_1_3, number = 1000): ["list  "],
        timeit.timeit(test5_2_3, number = 1000): ["tuple "],
        timeit.timeit(test5_3_3, number = 1000): ["set   "],
        timeit.timeit(test5_4_3, number = 1000): ["dict  "],
        timeit.timeit(test5_5_3, number = 1000): ["range "]
    }

    filename.write("\nTime for searching 10000: \n")
    slowest = list(reversed(sorted(test3.keys())))
    slowest = slowest[0]

    for p in reversed(sorted(test3)):
        filename.write(str(str(test3[p]) + str(slowest / p)))
        filename.write("\n")
