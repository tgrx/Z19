def normalized(Text):
    status = 0
    for element in Text:
        if element.isalnum():
            status = 1
    else:
        if not status:
            return ""

    will_deleted = []
    index = -1

    string = Text.split("/")
    string = list(filter(lambda x: x != "", string))
    string = list(filter(lambda y: y != ".", string))

    for i in string:
        index += 1
        if i == "..":
            will_deleted.append(index - 1)

    will_deleted.remove(-1)

    for i in reversed(will_deleted):
        string.pop(i)

    string = list(filter(lambda z: z != "..", string))

    return string


print(normalized(""))
