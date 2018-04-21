
f = open('/home/jenenliu/Desktop/copyface.txt')
for lines in f:
    print lines
f.close()
f = open('/home/jenenliu/Desktop/copyface.txt')
qc = lambda x: x.strip()
res = map(qc, f)

f.close()
print res