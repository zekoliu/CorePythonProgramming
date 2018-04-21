
firstfile = raw_input('Enter first filename: ')
secondfile = raw_input('Enter second filename: ')

f_file = open(firstfile, 'r')
s_file = open(secondfile, 'w')

for i in f_file:
    s_file.write(i)
f_file.close()
s_file.close()

f_file = open(firstfile, 'r')
s_file = open(secondfile, 'r')
print f_file.readlines(), s_file.readlines()
f_file.close()
s_file.close()
