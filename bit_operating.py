
start_num = int(raw_input('Enter start num: '))
end_num = int(raw_input('Enter end num: '))
print "DEC   BIN   OCT   HEX"
print '-----------------------'
for i in range(start_num, end_num + 1):
    print '%d\t' % i,
    print bin(i) + '\t',
    print '  %o\t' % i,
    print '  %x' % i