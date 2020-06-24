one, two, three = "aaaaaaaaa", "aaaaaaaaaaf", "aaaaaaaaaaaaaaaaaaaf"
# def runsInOnToThePowerOfmTimesnTime(stringOne, stringTwo, interwovenString):
#     if len(interwovenString) != len(stringOne) + len(stringTwo):
#         return False
#     return areInterwoven(stringOne, stringTwo, interwovenString, 0, 0)

# def areInterwoven(stringOne, stringTwo, interwovenString, i, j):
#     k = i + j
#     if k == len(interwovenString):
#         return True
#     print(stringOne, stringTwo, interwovenString, i, j)
#     if i < len(stringOne) and stringOne[i] == interwovenString[k]:
#         if areInterwoven(stringOne, stringTwo, interwovenString, i + 1, j):
#             return True

#     if j < len(stringTwo) and stringTwo[j] == interwovenString[k]:
#         return areInterwoven(stringOne, stringTwo, interwovenString, i, j + 1)


#     return False

def interwovenStrings(stringOne, stringTwo, interwovenString):
    if len(interwovenString) != len(stringTwo) + len(stringOne):
        return False
    cache = [[None for j in range(len(stringTwo) + 1)]
             for i in range(len(stringOne) + 1)]
    return areInterwoven(stringOne, stringTwo, interwovenString, 0, 0, cache)


def areInterwoven(stringOne, stringTwo, interwovenString, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(interwovenString):
        return True

    if i < len(stringOne) and stringOne[i] == interwovenString[k]:
        cache[i][j] = areInterwoven(
            stringOne, stringTwo, interwovenString, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(stringTwo) and stringTwo[j] == interwovenString[k]:
        cache[i][j] = areInterwoven(
            stringOne, stringTwo, interwovenString, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False


print(interwovenStrings(one, two, three))
