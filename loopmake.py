
dashes = '\n' + '-' * 50
exec_dict = {

    'f': """
    for %s in %s:
        print %s
    """,

    's': """
    %s = 0
    %s = %s
    while %s < len(%s):
        print %s[%s]
        %s = %s + 1
    """,

    'n':"""
    %s = %d
    while %s < %d:
        print %s
        %s = %s + %d
    """
}

def main():
    ltype = raw_input('Loop type?(For/While) ')
    dtype = raw_input('Data type?(Number/seq) ')

    if dtype == '\n':
        start = input('Starting values? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Steeping value? ')
        seq = str(range(start, stop, step))

    else:
        seq = raw_input('Enter sequence: ')
        var = raw_input('Iterative variable name? ')

        if ltype == 'f':
            exec_str = exec_dict['f'] % (var, seq, var)
        elif ltype == 'w':
            if dtype == 's':
                svar = raw_input('Enter sequence name? ')
                exex_str = exec_dict['%s'] % (var, svar, var, svar, svar, var, var, var)
            elif dtype == 'n':
                exec_str = exec_dict['n'] % (var, start, var, stop, var, var, step)

    print dashes
    print 'Your custom-generated code：' + dashes
    print exec_str + dashes
    print 'Test execuation of the code: ' + dashes
    print exec_str
    print dashes

if __name__ == '__main__':
    main()