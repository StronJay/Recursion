test = [
    9,
    [2, -3, 4],
    1,
    [1, 1, [1, 1, 1]],
    [[[[3, 4, 1]]], 8],
    [1, 2, 3, 4, 5, [6, 7], -7],
    [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
    [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]],
    -3
]


def productSum(array, multiplier=1):
    recursiveSum = 0
    for element in array:
        print(element, "multiplier:", multiplier, "currentSum", recursiveSum)
        if type(element) is list:
            recursiveSum += productSum(element, multiplier + 1)
        else:
            recursiveSum += element
    return recursiveSum * multiplier


print(productSum(test))
