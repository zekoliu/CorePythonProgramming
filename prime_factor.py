

def isprime(num):
    if num > 3 and num % 2 == 0:
        return False
    elif num > 3 and num % 3 == 0:
        return False
    elif num > 3 and num % 5 == 0:
        return False
    else:
        return True

def getfactors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

def showmenu(num):
    result = getfactors(num)
    for i in result:
        if not isprime(i):
            result.remove(i)
    return result

print showmenu(20)