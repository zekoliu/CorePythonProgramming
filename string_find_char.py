
def findchr(string, char):
    length = len(string)
    for i in range(length):
        if string[i] == char:
            return i;
    return -1

print findchr('kobe', 'e')

def rfindchar(string, char):
    length = len(string)
    for i in range(1, length):
        if string[length - i] == char:
            return (length - i)
    return -1

print rfindchar('ollolol', 'o')

def subchr(string, origchar, newchar):
    length = len(string)
    for i in range(length):
        if string[i] == origchar:
            origchar = newchar
            return origchar
    return -1

print subchr('kobe', 'e', 'zekoliu')
