def normalized(path: str) -> str:
    self = ""
    back = ""
    end = ""
    if path == "" or path == "." or path == "..":
        answer = ""
        return answer
    for i in range(0, len(path)):
        if path[i] == ".":
            continue
        self += path[i]
    for i in range(0, len(self)):
        if self[i] != "/" or i == 0:
            back += self[i]
        else:
            break
    back_text = self[::-1]
    for i in range(0, len(back_text)):
        if back_text[i] != "/" or i == 0:
            end += back_text[i]
        else:
            break
    end_text = end[::-1]
    if end_text == "/" and back != "/":
        answer = "/"
        return answer
    else:
        answer = ""
        return answer
    if back == "/":
        answer = ""
        return answer
    if back == "/" + end_text:
        answer = "/" + end_text
        return answer
    if back + "/" == "/" + end_text:
        answer = "/" + end_text
        return answer

    if end_text != "/":
        answer = back + "/" + end_text
    else:
        answer = back + end_text
    return answer


# print(normalized("../dfgh/"))
# print(normalized("/xxx/yyy/../zzz"))
# print(normalized("/xxx/./"))
# print(normalized("/a/b/./../c"))
print(normalized("../../../../../"))
