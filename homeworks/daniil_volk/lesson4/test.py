def reversed2(x):
    l = len(x)
    l = -1
    z = 0
    for e in range(l // 2):
        x[z], x[l] = x[l], [z]
        l = -1
        z = -1
    return list(x)


"""print(type(reversed2([1,2,3])))
y = reversed([1,2,3])
print(list(y))"""


assert list(reversed2([])) == []
# assert list(reversed2([3,2,1])) == [1,2,3]
assert list(reversed2([1, 1, 1])) == [1, 1, 1]
