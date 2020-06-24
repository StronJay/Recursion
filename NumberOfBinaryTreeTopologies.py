# def numberOfBinaryTreeTopologies(n):
#     cache = [1]
    
#     for m in range(1, n + 1):
#         numberOfTrees = 0
#         for leftTreeSize in range(m):
#             rightTreeSize = m - 1 - leftTreeSize
#             numberOfLeftTrees = cache[leftTreeSize]
#             numberOfRightTrees = cache[rightTreeSize]
#             #print(cache[leftTreeSize] , cache[rightTreeSize])
#             numberOfTrees += numberOfLeftTrees * numberOfRightTrees
#             #print(numberOfTrees, "Left Trees:", numberOfLeftTrees, "Right Trees:",numberOfRightTrees)
#         cache.append(numberOfTrees)
#     print(cache)
#     return cache[n]

def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    if n in cache:
        return cache[n]
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    cache[n] = numberOfTrees
    print(cache)
    return numberOfTrees

print(numberOfBinaryTreeTopologies(40))
