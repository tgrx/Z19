def compare_triplets(A, B):
    i = 0
    c = [0, 0]
    while i <= 2:
        if A[i] > B[i]:
            c[0] = c[0] + 1
        elif A[i] < B[i]:
            c[1] = c[1] + 1
        i += 1
    v = tuple(c)
    return v
