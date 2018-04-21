
filename = raw_input("Enter one file name: ")
filename = '/home/jenenliu/Desktop/' + filename + '.txt'
print filename
f = open(filename, 'r')

while True:
    for i in range(25):
        print f.next()
    print 'perss any key puls enter over.'
    enter_continue = raw_input('Press any key to continue: ')