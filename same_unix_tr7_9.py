
def tr(srcstr,dststr, string):
    srcstr = srcstr.lower()
    dststr = dststr.lower()
    string = string.lower()
    temp = ''
    for i in string:
        if i not in srcstr:
            temp = temp + i
    return dststr + temp

print tr('Abc', 'mno', 'abcdef')