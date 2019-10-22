def count_pnz(args):
    if len(args) == 0:
        return ("0.000000", "0.000000", "0.000000",)
    count_of_positives = 0
    count_of_negatives = 0
    count_of_nulls = 0
    for i in args:
        if i > 0:
            count_of_positives += 1
        if i < 0:
            count_of_negatives += 1
        if i == 0:
            count_of_nulls += 1
    count_of_positives = round(count_of_positives / len(args), 6)
    count_of_negatives = round(count_of_negatives / len(args), 6)
    count_of_nulls = round(count_of_nulls / len(args), 6)
    count_of_positives = str(count_of_positives).ljust(8, '0')
    count_of_negatives = str(count_of_negatives).ljust(8, '0')
    count_of_nulls = str(count_of_nulls).ljust(8, '0')
    return count_of_positives, count_of_negatives, count_of_nulls
