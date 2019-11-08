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
    step = 1
    string = ""

    for i in range(0, len(text)):
        if text[i].isalpha():
            string += "'" + text[i] + "'" + "*"
            try:
                while text[i + step].isdigit():
                    string += text[i + step]
                    step += 1
                else:
                    step = 1
                    string += " + "
            except IndexError:
                pass
    output = eval(string)
    return output

