
import sys

if sys.argv[1] == 'print':
    print 'Hello world!'
elif sys.argv[2] == '+' and len(sys.argv) > 2:
    print int(sys.argv[1]) + int(sys.argv[3])
elif sys.argv[2] == '-' and len(sys.argv) > 2:
    print int(sys.argv[1]) - int((sys.argv[3]))
elif sys.argv[2] == '*' and len(sys.argv) > 2:
    print int(sys.argv[1]) * int((sys.argv[3]))
elif sys.argv[2] == '/' and len(sys.argv) > 2:
    print int(sys.argv[1]) / int((sys.argv[3]))
elif sys.argv[2] == '^' and len(sys.argv) > 2:
    print int(sys.argv[1]) ^ int((sys.argv[3]))
