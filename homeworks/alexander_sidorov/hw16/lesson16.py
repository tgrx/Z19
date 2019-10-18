from typing import Text


def Zip(text: Text) -> Text:
    result = ""

    sequence_name = None
    length = 0

    for current in text:
        sequence_name = sequence_name or current

        if current == sequence_name:
            length += 1
            continue

        result += f"{sequence_name}{length}"
        length = 1
        sequence_name = current

    if sequence_name:
        result += f"{sequence_name}{length}"

    return result


def Unzip(text: Text) -> Text:
    result = ""

    ns = ""
    sequence_name = None

    for current in text:
        if current.isalpha():
            sequence_name = sequence_name or current

            if ns.isdecimal():
                if sequence_name:
                    result += sequence_name * int(ns)
                    ns = ""
                    sequence_name = current

        if current.isdecimal():
            ns += current

    if sequence_name and ns.isdecimal():
        result += sequence_name * int(ns)

    return result
