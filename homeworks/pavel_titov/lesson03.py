#уровень 2
import timeit
log = open("log.txt", "w")

def fix1():
    x = 100

def fix2():
    x =  100 * 200


def fix3():
    a = 500
    b = 100
    if a >= b:
        return a
    if b >= a:
        return b

def fix4():
    L = list("abc")
    L.append("d")
    L.extend("ehj")
    return L

def fix5():
    K = list("bbac")
    K.remove("b")
    K.remove("b")
    return K

def fix6():
    M = [1, 2, 3, 4, 7, 6, 5, 0, 9, 8]
    if M.index(2):
        return 2
    else:
        return ("Error")

def fix7():
    x = [1, 2, 3, 4, 7, 6, 5, 0, 9, 8]
    x.sort()
    return(x)



result = timeit.timeit("fix2()", setup="from __main__ import fix2")
log.write("SpeedTest2:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix3()", setup="from __main__ import fix3")
log.write("SpeedTest3:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix4()", setup="from __main__ import fix4")
log.write("SpeedTest4:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix5()", setup="from __main__ import fix5")
log.write("SpeedTest5:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix6()", setup="from __main__ import fix6")
log.write("SpeedTest6:")
log.write(str(result))
log.write("\n")

result = timeit.timeit("fix7()", setup="from __main__ import fix7")
log.write("SpeedTest7:")
log.write(str(result))
log.write("\n")
log.write("\n")

log.write(str(max(result)))

