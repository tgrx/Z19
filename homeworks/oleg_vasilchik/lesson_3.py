# 2 lvl
import timeit


def stat():
    s = """ int('00000')) = 2.37 ms ± 308 µs per loop 
            str(00000) = 2.8 ms ± 340 µs per loop       
            complex(1, 1) = 2.11 ms ± 323 µs per loop
            list(str(00000)) = 2.21 ms ± 350 µs per loop
            tuple([1, 2, 3]) = 2.01 ms ± 300 µs per loop
            x = [3, 2, 1]
            x.append(0)
            print(x) = 87.1 ns ± 6.38 ns per loop
            y = (1, 2,) + (3, 4)
            print(y)  # 79 ns ± 4.88 ns per loop
    """
    print(s)


stat()
