def tupleToDict(tuple: tuple | list, names: list[str]):
    i = 0
    result = dict()
    while( i < len(names)):
        result[names[i]] = tuple[i]
        i += 1
    return result