def compare_triplets(A, B):
    res = [0, 0]
    for x, y in zip(A, B):
        if x > y:
            res[0]+=1
        elif x < y:
            res[1]+=1
    return tuple(res)

