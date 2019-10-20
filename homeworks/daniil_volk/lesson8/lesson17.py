def compare_triplets(a, b):
    a_count = 0
    b_count = 0
    for i in range(3):
        if a[i] > b[i]:
            a_count += 1
        else:
            b_count += 1
    return a_count, b_count
