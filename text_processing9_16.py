
f = open('/home/jenenliu/Desktop/test.txt', 'r')
f_list = f.readlines()
f.close()

length = len(f_list)
for i in range(length):
    if len(f_list[i]) > 80:
        temp = f_list[i]
        f_list[i] = temp[:80] + '\n' + temp[80:]

f = open('/home/jenenliu/Desktop/test.txt', 'w')
for i in f_list:
    f.write(i)
f.close()
