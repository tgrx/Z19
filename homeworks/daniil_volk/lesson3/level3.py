def f(x, y=[]):
    y.append(x)
    return y


print(f(1))
print(f(1))
print(f(1))
print(f(1))
print(f(1))


"""while True:
  try:
     length = int(input("Enter length of list: "))
  except ValueError:
     continue
  else:
    if True:
     print("Length is available!")
     break


x = list()
while length > 0:  #my ubuntu has died when length raised to 1000000000, now I know why commit is need for
    x.append("a")
    length -= 1"""
