def count_pnz(args):
    count_of_positives = 0
    count_of_negatives = 0
    count_of_nulls = 0
    total_count = []
    for i in args:
        if i > 0:
            count_of_positives += 1
        if i < 0:
            count_of_negatives += 1
        else:
            count_of_nulls += 0
    total_count.append(str(count_of_positives / len(args)))
    total_count.append(str(count_of_negatives / len(args)))
    total_count.append(str(count_of_nulls / len(args)))
    return tuple(total_count)
