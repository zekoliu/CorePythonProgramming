def printf(fmt, *var):
    print fmt % var

printf('%d-%s-%s', 2016, '01', '06')

def prinf(*nkw):
    length = len(nkw)
    for eachnkw in nkw:
        eachnkw = str(eachnkw)
        if eachnkw == '%d':
            print eachnkw
            for i in range(length):
                print i
                if eachnkw.isdigit():
                    print nkw[i]
                    break
        elif eachnkw == '%f':
            for i in range(length):
                print i
                if eachnkw.isdigit():
                    print float(nkw[i])
                    break

prinf('%d, %f', 10, 90)