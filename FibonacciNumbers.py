# def recursiveFibonacci(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)


# def memoizeFibonacci(n, memoize={1: 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = memoizeFibonacci(n - 1, memoize) + memoizeFibonacci(n - 2, memoize)
#         return memoize[n]

def fibonacciNumbers(n):
    lastTwoCalculatedFibonacciNumbers = [0, 1]
    counter = 3
    while counter < n:
        nextFibonacciNumber = lastTwoCalculatedFibonacciNumbers[0] + lastTwoCalculatedFibonacciNumbers[1]
        lastTwoCalculatedFibonacciNumbers[0] = lastTwoCalculatedFibonacciNumbers[1]
        lastTwoCalculatedFibonacciNumbers[1] = nextFibonacciNumber
        counter += 1
    return lastTwoCalculatedFibonacciNumbers[1] if n > 2 else 0

print(fibonacciNumbers(300000))