test = [1, 2, 3, 4, 5]


# def powerset(array):
#     subsets = [[]]
#     for element in array:
#         for i in range(len(subsets)):
#             currentSubset = subsets[i]
#             subsets.append(currentSubset + [element])
#     return subsets


def powerset(array, i=None):
    if i is None:
        i = len(array) - 1
    if i < 0:
        return [[]]
    ele = array[i]
    subsets = powerset(array, i - 1)
    for j in range(len(subsets)):
        currentSubset = subsets[j]
        subsets.append(currentSubset + [ele])
    return subsets
    


print(powerset(test))
