
isExit = True
filename = 'newfile'
while isExit:
    select = int(raw_input("1: new file, 2: print file, 3: editor file, 4: save file, 5: exit: "))

    if select == 1:
        filename = raw_input("Enter one filename: ")
        content = raw_input("Enter file content: ")
        f = open(filename, 'w')
        f.write(content)
        f.close()
    elif select == 2:
        f = open(filename, 'r')
        for i in f:
            print i
        f.close()
    elif select == 3:
        content = raw_input(('Enter filename content: '))
        f = open(filename, 'w')
        f.write(content)
        f.close()
    elif select == 4:
        print 'save successful!!!'
    elif select == 5:
        print 'exit success'
        isExit = False