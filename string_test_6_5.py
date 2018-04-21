
a = 'eefffeeff'

length = len(a)

if (length % 2 == 0):
    half = length / 2
    if a[:half] == a[half:]:
        print "true"
    else:
        print 'false'
else:
    half = length / 2
    if a[:half] == a[half+1:]:
        print 'true'
    else:
        print 'false'


# a = 'kobe'
# b = 'kobe'
#
# i = 0
# if len(a) != len(b):
#     print 'Mismatch'
# else:
#     for n in a:
#         if n != b[i]:
#             print 'Mismatch'
#             break
#         i += 1
#     if (i == len(a)):
#         print "you are right"

