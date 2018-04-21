
import time

def timeit(function):
    start_time = time.time()
    result = function
    end_time = time.time()
    return  (result, end_time - start_time)

def mult(x, y):
    return x * y

# result = reduce(mult, range(1,3))
# print result# print reduce(mult, range(9)[1:])

def factorial(number):
    result = reduce((lambda x,y: x*y), range(1, number+1))
    return result

def iteration(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * recursive(n-1)
print timeit(factorial(9))
print timeit(iteration(9))
print timeit(recursive(9))