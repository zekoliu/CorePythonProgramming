
input_num = int(raw_input("Enter total number of names: "))
mistakenum = 0
name_list =[]
for i in range(input_num):
    name = raw_input('please enter name %d: ' % i)
    if ',' not in name:
        mistakenum+=1
        print 'Wrong format... shpuld be, Last /' \
              'You have done this %d time(s) already, Fixing input...' % mistakenum
        length = len(name)
        for spaceindex in range(length):
            if name[spaceindex] == ' ':
                name = name[:spaceindex] + ',' + name[spaceindex:];
                break
    name_list.append(name)

print 'The sorted list (by last name) is:\n', sorted(name_list)