def normalized(path: str) -> str:
    self = ""
    back = ""
    end = ""
    z = len(path) - 1
    e = len(path) - 2
    if path == "" or path == "." or path == "..":
        answer = ""
        return answer
    elif path[0] == "." and path[1] != "." and path[z] == "." and path[e] != ".":
        answer = "/"
        return answer
    elif path[0] == "." and path[1] == "/" and path[z] == "/" and path[e] == ".":
        answer = "/"
        return answer
    elif path[0] == "." and path[1] == "/" and path[z] == "." and path[e] == ".":
        answer = path[2] + path[3] + path[4] + path[5]
        return answer
    elif path[0] == "/" and path[1] == "." and path[z] == "/" and path[e] == ".":
        answer = "/"
        return answer
    elif path[0] == "/" and path[1] == "." and path[z] == "/" and path[e] != ".":
        answer = "/" + path[e - 3] + path[e - 2] + path[e - 1] + path[e] + "/"
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
    if path[0] == "." and path[1] == "." and path[z] == "/" and path[e] != ".":
        answer = back + "/"
        return answer
    if path[0] == "." and path[e] != "." and path[z] == "/":
        answer = back
        return answer
    if back == "/":
        answer = ""
        return answer
    if back == "/" + end_text or back + "/" == "/" + end_text:
        answer = "/" + end_text
        return answer
    if end_text != "/":
        answer = back + "/" + end_text
    else:
        answer = back + end_text
    return answer


# print(normalized("abc/def/"))           # abc/def/
# print(normalized("/xxx/yyy/../zzz"))    # /xxx/zzz
# print(normalized("/xxx/./"))            # /xxx/
# print(normalized("/a/b/./../c"))        # /a/c
# print(normalized("../../../../../"))    #
# print(normalized("../mrbi"))            # /mrbi
# print(normalized("../movz/"))           # /movz/
# print(normalized("./../../../../"))       # /
# print(normalized("./uags/./././././uags/.."))  # uags
# print(normalized("/../../../../"))     # /
# print(normalized("/.././.././../pwjq/.././.././../pwjq/")) # /pwjq/
