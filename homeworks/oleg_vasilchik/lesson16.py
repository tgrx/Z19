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
        if text[i].isalpha():
            data = text[i] * int(text[i + 1])
            if text[i+2].isdigit():
                data = text[i] * int(text[i+1] + text[i+2])
            output.append(data)

    return "".join(output)
