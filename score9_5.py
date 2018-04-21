
socorelist = []

while True:
    overinput = int(raw_input("Enter 1 to continue, Enter 0 to over: "))
    if overinput == 0:
        break

    elif overinput == 1:
        filename = raw_input('Enter one file name: ')
        f = open(filename, 'r')
        for i in f.readline():
            socorelist.append(i)

print socorelist,
sum = 0
for eachList in socorelist:
    if eachList != '\n':
        sum =sum + int(eachList)

print (int)(sum / len(socorelist))