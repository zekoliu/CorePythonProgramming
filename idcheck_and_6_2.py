
import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Check v1.0'
print 'Testees must be at least 2 chars long.'
myIntput = raw_input('Identifier to test? ')

if len(myIntput) > 1:

    if myIntput in keyword.kwlist:
        print 'invaild: is keyword'

    elif myIntput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''

    else:
        for otherChar in myIntput[1:]:

            if otherChar not in alphas:
                print '''invalid: remaining symbols must be alphanumeric'''
                break
        else:
            print 'okay as an identifier'
elif len(myIntput) == 1:
    if (not myIntput.isdigit()):
        print 'okay as an identifier'