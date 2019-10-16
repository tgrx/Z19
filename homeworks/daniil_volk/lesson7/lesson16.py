def Zip(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError
    first_coin = (None, None)
    zipped_text = ""
    for char in enumerate(text):
        if char[1] != first_coin[1]:
            if char[0] != 0:
                zipped_text += str(first_coin[1] + str(char[0] - first_coin[0]))
            first_coin = char
        if char[0] == len(text) - 1:
            zipped_text += str(first_coin[1] + str((char[0] - first_coin[0]) + 1))
    return zipped_text


def Unzip(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError
    current_char = ""
    unzipped_text = ""
    number = ""
    for char in enumerate(text):
        if char[1].isalpha():
            if number != "":
                unzipped_text += current_char * int(number)
            current_char = char[1]
            number = ""
        else:
            number += char[1]
        if char[0] == len(text) - 1:
            unzipped_text += current_char * int(number)
    return unzipped_text
