import re


def normalized(path):
    if not re.search(r"\w", path):
        return ""
    normalized = path.replace("/./", "")
    normalized = normalized.split("/")
    for i in normalized:
        if ".." in i:
            normalized.remove(i)
    normalized = "/".join(normalized)
    return normalized
