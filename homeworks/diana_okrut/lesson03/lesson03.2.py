import timeit
from decimal import Decimal


f = open('results.txt', 'w')

a = Decimal('0.33') + Decimal('1.66')
b = Decimal(5**7) + Decimal(7**5)
c = Decimal(17**19) + Decimal(19**17)
f.write(f' lead time 5**7 + 7**5              ---> {timeit.timeit("5**7 + 7**5")} \n')
f.write(f' lead time 17**19 + 19**17          ---> {timeit.timeit("17**19 + 19**17")} \n')
f.write(f' lead time 1e30 + 1e-30             ---> {timeit.timeit("1e30 + 1e-30")} \n')
f.write(f' lead time 1+2j + 2-1j              ---> {timeit.timeit("1+2j + 2-1j")} \n')
f.write(f' lead time Decimal: "0.33" + "1.66" ---> {timeit.timeit(f"{a}")} \n')
f.write(f' lead time Decimal: 5**7 + 7**5     ---> {timeit.timeit(f"{b}")} \n')
f.write(f' lead time Decimal: 17**19 + 19**17 ---> {timeit.timeit(f"{c}")} \n \n')

a = Decimal('0.33') * Decimal('1.66')
b = Decimal(5**7) * Decimal(7**5)
c = Decimal(17**19) * Decimal(19**17)
f.write(f' lead time 5**7 * 7**5              ---> {timeit.timeit("5**7 * 7**5")} \n')
f.write(f' lead time 17**19 * 19**17          ---> {timeit.timeit("17**19 * 19**17")} \n')
f.write(f' lead time 1e30 * 1e-30             ---> {timeit.timeit("1e30 * 1e-30")} \n')
f.write(f' lead time 1+2j * 2-1j              ---> {timeit.timeit("1+2j * 2-1j")} \n')
f.write(f' lead time Decimal: "0.33" * "1.66" ---> {timeit.timeit(f"{a}")} \n')
f.write(f' lead time Decimal: 5**7 * 7**5     ---> {timeit.timeit(f"{b}")} \n')
f.write(f' lead time Decimal: 17**19 * 19**17 ---> {timeit.timeit(f"{c}")} \n \n')

a = Decimal('0.33') / Decimal('1.66')
b = Decimal(5**7) / Decimal(7**5)
c = Decimal(17**19) / Decimal(19**17)
f.write(f' lead time 5**7 / 7**5              ---> {timeit.timeit("5**7 / 7**5")} \n')
f.write(f' lead time 17**19 / 19**17          ---> {timeit.timeit("17**19 / 19**17")} \n')
f.write(f' lead time 1e30 / 1e-30             ---> {timeit.timeit("1e30 / 1e-30")} \n')
f.write(f' lead time 1+2j / 2-1j              ---> {timeit.timeit("1+2j / 2-1j")} \n')
f.write(f' lead time Decimal: "0.33" / "1.66" ---> {timeit.timeit(f"{a}")} \n')
f.write(f' lead time Decimal: 5**7 / 7**5     ---> {timeit.timeit(f"{b}")} \n')
f.write(f' lead time Decimal: 17**19 / 19**17 ---> {timeit.timeit(f"{c}")} \n \n')

s = 'ab' * 10000 + 'c'
f.write("s = 'ab' * 10000 + 'c' \n")
f.write(f' lead time "a" in s                     ---> {timeit.Timer("a" in f"{s}")} \n')
f.write(f' lead time "b" in s                     ---> {timeit.Timer("b" in f"{s}")} \n')
f.write(f' lead time "c" in s                     ---> {timeit.Timer("c" in f"{s}")} \n')
f.write(f' lead time "ab" in s                    ---> {timeit.Timer("ab" in f"{s}")} \n')
f.write(f' lead time "ba" in s                    ---> {timeit.Timer("ba" in f"{s}")} \n')
f.write(f' lead time "bc" in s                    ---> {timeit.Timer("bc" in f"{s}")} \n')
f.write(f' lead time "ac" in s                    ---> {timeit.Timer("ac" in f"{s}")} \n')
f.write(f' lead time "ababababababababababc" in s ---> {timeit.Timer("ababababababababababc" in f"{s}")} \n \n')


L = [i for i in range(10000)]
# f.write(f' lead time 0 in L ---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 9999 in L---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 10000 in L---> {timeit.timeit("1+2j + 2-1j")} "\n"')


T = tuple(i for i in range(10000))
# f.write(f' lead time 0 in T ---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 9999 in T---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 10000 in T---> {timeit.timeit("1+2j + 2-1j")} "\n"')


S = {i for i in range(10000)}
# f.write(f' lead time 0 in S ---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 9999 in S---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 10000 in S---> {timeit.timeit("1+2j + 2-1j")} "\n"')


D = {i:i for i in range(10000)}
# f.write(f' lead time 0 in D ---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 9999 in D---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 10000 in D---> {timeit.timeit("1+2j + 2-1j")} "\n"')


R = range(10000)
# f.write(f' lead time 0 in R ---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 9999 in R---> {timeit.timeit("1+2j + 2-1j")} "\n"')
# f.write(f' lead time 10000 in R---> {timeit.timeit("1+2j + 2-1j")} "\n""\n"')


f.close()
