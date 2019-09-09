import timeit
from decimal import Decimal

f = open("timeit_log.txt", "w")
def sec(s):
  #  print(s, timeit.timeit(s, number=10000), "cek")
    return (timeit.timeit(s, number=10000))

f.write("   --- Сложение ---  \n")
plus = sec("int(5**7+7**5)")
f.write("int(5**7+7**5)  -  "f'{plus}'" sec \n")
plus = sec("int(17**19+19**17)")
f.write("int(17**19+19**17)  -  "f'{plus}'" sec \n")
plus = sec("float(1e30+1e-30)")
f.write("float(1e30+1e-30) -  "f'{plus}'" sec \n")
plus = sec("complex (1+2j + 2-1j)")
f.write("complex (1+2j + 2-1j -  "f'{plus}'" sec \n")
x = Decimal("1.33") + Decimal("1.22")
plus = sec(f'{x}')
f.write("Decimal('1.33') + Decimal('1.22') -  "f'{plus}'" sec \n")
y = Decimal(5**7) + Decimal(7**5)
plus = sec(f'{y}')
f.write("Decimal(5**7) + Decimal(7**5) -  "f'{plus}'" sec \n")
z = Decimal(17**19) + Decimal(19**17)
plus = sec(f'{z}')
f.write("Decimal(17**19) + Decimal(19**17) -  "f'{plus}'" sec \n\n")

f.write("   --- Умножение ---  \n")
m = sec("int(5**7*7**5)")
f.write("int(5**7*7**5)  -  "f'{m}'" sec \n")
m = sec("int(17**19*19**17)")
f.write("int(17**19*19**17)  -  "f'{m}'" sec \n")
m = sec("float(1e30*1e-30)")
f.write("float(1e30*1e-30) -  "f'{m}'" sec \n")
m = sec("complex (1+2j * 2-1j)")
f.write("complex (1+2j * 2-1j -  "f'{m}'" sec \n")
x = Decimal("1.33") * Decimal("1.22")
m = sec(f'{x}')
f.write("Decimal('1.33') * Decimal('1.22') -  "f'{m}'" sec \n")
y = Decimal(5**7) * Decimal(7**5)
m = sec(f'{y}')
f.write("Decimal(5**7) * Decimal(7**5) -  "f'{m}'" sec \n")
z = Decimal(17**19) * Decimal(19**17)
m = sec(f'{z}')
f.write("Decimal(17**19) * Decimal(19**17) -  "f'{m}'" sec \n\n")

f.write("   --- Деление ---  \n")
d = sec("int(5**7/7**5)")
f.write("int(5**7/7**5)  -  "f'{d}'" sec \n")
d = sec("int(17**19/19**17)")
f.write("int(17**19/19**17)  -  "f'{d}'" sec \n")
d = sec("float(1e30/1e-30)")
f.write("float(1e30/1e-30) -  "f'{d}'" sec \n")
d = sec("complex (1+2j / 2-1j)")
f.write("complex (1+2j / 2-1j -  "f'{d}'" sec \n")
x = Decimal("1.33") / Decimal("1.22")
d = sec(f'{x}')
f.write("Decimal('1.33') * Decimal('1.22') -  "f'{d}'" sec \n")
y = Decimal(5**7) / Decimal(7**5)
d = sec(f'{y}')
f.write("Decimal(5**7) / Decimal(7**5) -  "f'{d}'" sec \n")
z = Decimal(17**19) / Decimal(19**17)
d = sec(f'{z}')
f.write("Decimal(17**19) / Decimal(19**17) -  "f'{d}'" sec \n\n")

f.write("   ---  Строки ---  \n")
s = "ab" * 10000 + "c"
a = timeit.timeit(f'"a" in "{s}"')
b = timeit.timeit(f'"b" in "{s}"')
c = timeit.timeit(f'"c" in "{s}"')
ab = timeit.timeit(f'"ab" in "{s}"')
ba = timeit.timeit(f'"ba" in "{s}"')
bc = timeit.timeit(f'"bc" in "{s}"')
ac = timeit.timeit(f'"ac" in "{s}"')
ababababababababababc = timeit.timeit(f'"ababababababababababc" in "{s}"')
f.write("s = 'ab' * 10000 + 'c' \n")
f.write("a in s "f'{a}'" sec \n")
f.write("b in s "f'{b}'" sec \n")
f.write("c in s "f'{c}'" sec \n")
f.write("ab in s "f'{ab}'" sec \n")
f.write("ba in s "f'{ba}'" sec \n")
f.write("bc in s "f'{bc}'" sec \n")
f.write("ac in s "f'{ac}'" sec \n")
f.write("ababababababababababc in s "f'{ababababababababababc}'" sec \n\n")

f.write("   ---  Коллекции ---  \n")
f.write("   ---  В списке ---  \n")
L = [i for i in range(10000)]
a = timeit.timeit(f'"0" in "{L}"')
f.write("0 in L - "f'{a}'" sec \n")
b = timeit.timeit(f'"999" in "{L}"')
f.write("9999 in L - "f'{b}'" sec \n")
c = timeit.timeit(f'"1000" in "{L}"')
f.write("10000 in L - "f'{c}'" sec \n\n")

f.write("   ---  В кортеже ---  \n")
T = tuple(i for i in range(10000))
a = timeit.timeit(f'"0" in "{T}"')
f.write("0 in T - "f'{a}'" sec \n")
b = timeit.timeit(f'"999" in "{T}"')
f.write("9999 in T - "f'{b}'" sec \n")
c = timeit.timeit(f'"1000" in "{T}"')
f.write("10000 in T - "f'{c}'" sec \n\n")

f.write("   ---  Во множестве ---  \n")
S = {i for i in range(10000)}
a = timeit.timeit(f'"0" in "{S}"')
f.write("0 in S - "f'{a}'" sec \n")
b = timeit.timeit(f'"999" in "{S}"')
f.write("9999 in S - "f'{b}'" sec \n")
c = timeit.timeit(f'"1000" in "{S}"')
f.write("10000 in S - "f'{c}'" sec \n\n")

f.write("   ---  В словаре ---  \n")
D = {i:i for i in range(10000)}
a = timeit.timeit(f'"0" in "{D}"')
f.write("0 in D - "f'{a}'" sec \n")
b = timeit.timeit(f'"999" in "{D}"')
f.write("9999 in D - "f'{b}'" sec \n")
c = timeit.timeit(f'"1000" in "{D}"')
f.write("10000 in D - "f'{c}'" sec \n\n")

f.write("   ---  В рэнже ---  \n")
R = range(10000)
a = timeit.timeit(f'"0" in "{R}"')
f.write("0 in R - "f'{a}'" sec \n")
b = timeit.timeit(f'"999" in "{R}"')
f.write("9999 in R - "f'{b}'" sec \n")
c = timeit.timeit(f'"1000" in "{R}"')
f.write("10000 in R - "f'{c}'" sec \n\n")
f.close()
