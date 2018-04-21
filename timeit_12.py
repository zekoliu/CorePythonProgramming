
import time

def timeit(function):
    start_time = time.time()
    result = function
    end_time = time.time()
    return  (result, end_time - start_time)

def fuck(x, y):
    return x*y
    # print 'what the fuck!'

print timeit(fuck)
