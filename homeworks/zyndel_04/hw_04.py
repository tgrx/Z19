a = {
    "zyndel": "qwerty",
    "master": 123,
    "alexander": "*12qw",
    "artem": 55567,
    "egor": [1, 5, 7],
    "lol": 17,
    "bugaGA": (1, 3, 6),
}
print("bugaGA" in a)
a["egor"].append(4)
print(a)
# %timeit 'bugaGA' in a       # 53.8 ns
# %timeit a['egor'].append(4) #123 ns

#####################
b = 48
c = 54
print(b ** c)
print(b > c)
print((b - c) * b)
# %timeit b ** c      # 830 ns
# %timeit b > c       # 67.2 ns
# %timeit (b - c) * b # 135 ns

######################
d = "xyz"
e = "zyx"
print(d == e)
print(d + e)
# %timeit d == e # 73 ns
# %timeit d + e  # 120 ns

#####################
f = [1, 4, 5, 8, 66, 1, 35, 778, 952, 4, 3]
print(f[6])
# %timeit f[6]       # 52.4 ns
f.sort()
print(f)
del f[1:8]
print(f)
# %timeit f.sort()   # 127 ns
# %timeit del f[1:8] # 104 ns

###############
g = "HelloMyDearFriend"
i = list(g)
print(i)
# %timeit list(g) # 444 ns
