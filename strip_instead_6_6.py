
a = '      jorth       '

length = len(a)
index = 0
space = ' '
for i in range(length):
    if a[i] != ' ':
        a = a[i:]
        index = i
    if (i > index):
        if a[i] == space:
            lastindex = i
print a[index:lastindex]

