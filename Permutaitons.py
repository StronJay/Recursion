test = [1, 2, 3, 4, 5, 6]


# def getPermutations(array):
#     permutations = []
#     permutationsHelper(array, [], permutations)
#     return permutations


# def permutationsHelper(array, currentPermutation, permutations):
#     if not len(array) and len(currentPermutation): # The only reason you have len(currentPermutation) is if it has [] as an input. Who does that?! w/e
#         permutations.append(currentPermutation)
        
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] + array[i + 1:]
#             newPermutation = currentPermutation + [array[i]]
#             print("newArr:", newArray, "newPerm:", currentPermutation, "+", [array[i]], "i      ", i)
#             permutationsHelper(newArray, newPermutation, permutations)

def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations

def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:]) #SNAPSHOT!!!!
    for j in range(i, len(array)):
        array[i], array[j] = array[j], array[i]
        permutationsHelper(i + 1, array, permutations)
        array[i], array[j] = array[j], array[i]

print(getPermutations(test))