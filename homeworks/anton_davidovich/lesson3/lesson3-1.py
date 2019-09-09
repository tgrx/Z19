import timeit

int1 = 5 ** 7
int2 = 7 ** 5

def test1_1():
    return int1 + int2


print(timeit.timeit(test1_1, number=1000))

int3 = 17**19
int4 = 19**17

def test1_2():
    return int3 + int4

print(timeit.timeit(test1_2, number=1000))

int5 = 1e30
int6 = 1e-30

def test1_3():
    return int5  + int6

print(timeit.timeit(test1_3, number=1000))

int7 = 1 + 2j
int8 = 1 - 2j

def test1_4():
    return int7 + int8

print(timeit.timeit(test1_4, number=1000))

int9 = 0.33
int10 = 1.66

def test1_5():
    return int9 + int10

print(timeit.timeit(test1_5, number=1000))

int11 = 5.0 ** 7.0
int12 = 7.0 ** 5.0

def test1_6():
    return int11 + int12

print(timeit.timeit(test1_6, number=1000))

int13 = 17.0 ** 19.0
int14 = 19.0 ** 17.0

def test1_7():
    return int13 + int14

print(timeit.timeit(test1_7, number=1000))

int1 = 5 ** 7
int2 = 7 ** 5

def test2_1():
    return int1 * int2

print(timeit.timeit(test2_1, number=1000))

int3 = 17**19
int4 = 19**17

def test2_2():
    return int3 * int4

print(timeit.timeit(test2_2, number=1000))

int5 = 1e30
int6 = 1e-30

def test2_3():
    return int5 * int6

print(timeit.timeit(test2_3, number=1000))

int7 = 1 + 2j
int8 = 1 - 2j

def test2_4():
    return int7 * int8

print(timeit.timeit(test2_4, number=1000))

int9 = 0.33
int10 = 1.66

def test2_5():
    return int9 * int10

print(timeit.timeit(test2_5, number=1000))

int11 = 5.0 ** 7.0
int12 = 7.0 ** 5.0

def test2_6():
    return int11 * int12

print(timeit.timeit(test2_6, number=1000))

int13 = 17.0 ** 19.0
int14 = 19.0 ** 17.0

def test2_7():
    return int13 * int14

print(timeit.timeit(test2_7, number=1000))

int1 = 5 ** 7
int2 = 7 ** 5

def test3_1():
    return int1 / int2

print(timeit.timeit(test3_1, number=1000))

int3 = 17**19
int4 = 19**17

def test3_2():
    return int3 / int4

print(timeit.timeit(test3_2, number=1000))

int5 = 1e30
int6 = 1e-30

def test3_3():
    return int5 / int6

print(timeit.timeit(test3_3, number=1000))

int7 = 1 + 2j
int8 = 1 - 2j

def test3_4():
    return int7 / int8

print(timeit.timeit(test3_4, number=1000))

int9 = 0.33
int10 = 1.66

def test3_5():
    return int9 / int10

print(timeit.timeit(test3_5, number=1000))

int11 = 5.0 ** 7.0
int12 = 7.0 ** 5.0

def test3_6():
    return int11 / int12

print(timeit.timeit(test3_6, number=1000))

int13 = 17.0 ** 19.0
int14 = 19.0 ** 17.0

def test3_7():
    return int13 / int14

print(timeit.timeit(test3_7, number=1000))

s = "ab" * 10000 +"c"

def test4_1():
    return "a" in s

print(timeit.timeit(test4_1, number=1000))

def test4_2():
    return "b" in s
print(timeit.timeit(test4_2, number=1000))

def test4_3():
    return "c" in s

print(timeit.timeit(test4_3, number=1000))

def test4_4():
    return "c" in s

print(timeit.timeit(test4_4, number=1000))

def test4_5():
    return "ab" in s

print(timeit.timeit(test4_5, number=1000))

def test4_6():
    return "ba" in s

print(timeit.timeit(test4_6, number=1000))

def test4_7():
    return "bc" in s

print(timeit.timeit(test4_7, number=1000))

def test4_8():
    return "ac" in s

print(timeit.timeit(test4_8, number=1000))

def test4_9():
    return "ababababababababababc" in s

print(timeit.timeit(test4_8, number=1000))

L = [i for i in range(10000)]

def test5_1():
    return 0 in L

print(timeit.timeit(test5_1, number=1000))

def test5_2():
    return 9999 in L

print(timeit.timeit(test5_2, number=1000))

def test5_3():
    return 10000 in L

print(timeit.timeit(test5_3, number=1000))

T = tuple(i for i in range(10000))

def test6_1():
    return 0 in T

print(timeit.timeit(test6_1, number=1000))

def test6_2():
    return 9999 in T

print(timeit.timeit(test6_1, number=1000))

def test6_3():
    return 10000 in T

print(timeit.timeit(test6_3, number=1000))

S = {i for i in range(10000)}

def test7_1():
    return 0 in S

print(timeit.timeit(test7_1, number=1000))

def test7_2():
    return 9999 in S

print(timeit.timeit(test7_2, number=1000))

def test7_3():
    return 10000 in S

print(timeit.timeit(test7_3, number=1000))

