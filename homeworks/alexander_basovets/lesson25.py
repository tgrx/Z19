def normalized(path: str) -> str:
    self = ""
    answer = ""
    #  if path != "../../../..":
    for i in range(0, len(path)):
        if path[i] == ".":
            continue
        self += path[i]
    for i in range(0, len(self)):
        if i == len(self) - 1:
            if path[i] == "/":
                answer += self[i]
                break
        if self[i] == "/":
            if self[i + 1] == "/":
                continue
        answer += self[i]
    position = self.rfind("/")
    # answer += self[position+1:]
    #   else:
    #       answer = ""
    return answer


# print(normalized("../../../.."))
