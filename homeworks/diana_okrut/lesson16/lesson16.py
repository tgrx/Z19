def Zip(text):
    if not text:
        return text

    letter = text[0]
    counter = 0
    answer = ''
    buffer = []

    for i in text:
        if letter == i:
            counter += 1
            buffer = [letter, f'{counter}']
        else:
            answer += ''.join(buffer)
            counter = 1
            buffer = [i, f'{counter}']
            letter = i

    answer += ''.join(buffer)
    return answer


def Unzip(text):
    if not text:
        return text

    answer = ''
    letter = text[0]
    quantity = ''
    buffer = [letter, quantity]

    for i in text:
        if i == letter:
            buffer[0] = i
        elif i.isdigit():
            quantity += i
            buffer[1] = quantity
        else:
            answer += buffer[0] * int(buffer[1])
            letter = i
            quantity = ''
            buffer = [letter, quantity]
    answer += buffer[0] * int(buffer[1])
    return answer
