def Zip(text):
    output = []
    letters_counter = dict()

    for i in text:
        if i in letters_counter:
            letters_counter[i] += 1
        else:
            letters_counter.update({i: 1})

    for i in letters_counter:
        output.append(i)
        output.append(str(letters_counter[i]))

    return "".join(output)


def Unzip(text):
    output = []

    for i in range(0, len(text)):
        if i % 2 == 0:
            data = text[i] * int(text[i + 1])
            output.append(data)
    return "".join(output)




