def compare_triplets(A, B):
    output = []
    score_a = 0
    score_b = 0

    for a, b in zip(A, B):
        if a > b:
            score_a += 1
        else:
            score_b += 1

    output.append(score_a)
    output.append(score_b)

    return tuple(output)
