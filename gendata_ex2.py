
from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

f = open('redata.txt', 'w')
for i in range(randint(5, 10)):
    dtint = randint(0, 1000)
    dtstr = ctime(dtint)
    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)
    result = '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
    f.write(result + '\n')
f.close()
    # print result #'%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
