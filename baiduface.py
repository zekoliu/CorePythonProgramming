import os
ls = os.linesep

while True:

    if os.path.exists():
        print "Error: '%s' alread exists" % '/home/jenenliu/Desktop/test.txt'
    else:
        break

all = []
print "\nEnter lines ('.' by itself to quit).\n"

while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open('/home/jenenliu/Desktop/test.txt', 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE'
