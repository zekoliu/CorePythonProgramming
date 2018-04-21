
import math
import cmath

def safe_sqrt(number):
    try:
        result = math.sqrt(number)
    except ValueError:
        result = cmath.sqrt(number)
    return result

if __name__ == '__main__':
    print safe_sqrt(-9)