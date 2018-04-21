
import re

month_num = [0,0,0,0,0,0,0,0,0,0,0,0]

mon_re = '-\d*-'
f = open('redata.txt', 'r')
for i in f.readlines():
    m = re.search(mon_re, i).group()
    if m == '-1-':
        month_num[0] += 1
    elif m == '-2-':
        month_num[1] += 1
    elif m == '-3-':
        month_num[2] += 1
    elif m == '-4-':
        month_num[3] += 1
    elif m == '-5-':
        month_num[4] += 1
    elif m == '-6-':
        month_num[5] += 1
    elif m == '-7-':
        month_num[6] += 1
    elif m == '-8-':
        month_num[7] += 1
    elif m == '-9-':
        month_num[8] += 1
    elif m == '-9-':
        month_num[8] += 1
    elif m == '-10-':
        month_num[9] += 1
    elif m == '-11-':
        month_num[10] += 1
    elif m == '-12-':
        month_num[11] += 1
f.close()
for i in range(len(month_num)):
    print (i+1),'month', month_num[i], 'times'