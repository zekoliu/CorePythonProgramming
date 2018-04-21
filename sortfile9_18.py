
ch = raw_input('Enter one char: ')
filename = raw_input(('Enter one filename: '))
ch_count = 0

f = open(filename, 'r')
for eachLine in f:
    for eachWord in eachLine:
        if eachWord == ch:
            ch_count+=1

print ch_count