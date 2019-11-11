def normalized(path):
    normalized = path.replace("/./", "")
    normalized = normalized.split('/')
    for i in normalized:
        if '..' in i:
            normalized.remove(i)
    normalized = '/'.join(normalized)
    return normalized