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
    if not text:
        return ""
    step = 1
    output = ""

    for i in range(0, len(text)):
        if text[i].isalpha():
            output += "'" + text[i] + "'" + "*"
            try:
                while text[i + step].isdigit():
                    output += text[i + step]
                    step += 1
                else:
                    step = 1
                    output += " + "
            except IndexError:
                pass
    return eval(output)
