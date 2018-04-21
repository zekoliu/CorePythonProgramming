
firstfile = raw_input("Enter first filename: ")
secondfile = raw_input("Enter second filename: ")

firstlist = []
secondlist = []

first_f = open(firstfile, 'r')
for i in first_f:
    firstlist.append(i)
second_f = open(secondfile, 'r')
for i in second_f:
    secondlist.append(i)

f_length = len(firstlist)
s_length = len(secondlist)

nosamelinenum = []
if f_length > s_length:
    for i in range(s_length):
        if firstlist[i] != secondlist[i]:
            nosamelinenum.append(i)
else:
    for i in range(f_length):
        if firstlist[i] != secondlist[i]:
            nosamelinenum.append(i)

print nosamelinenum