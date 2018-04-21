
import re
# k = 'Thu Jan  1 00:01:01 1970'
data = '\w+\s\w+\s+\d\s\d+:\d+:\d+\s\d+' #19
email = '\w+@\w+(.com|.net|.edu|.org|.gov)' #20
month = '-\w+-' #21
year = '\w+-' #22
time_value  = '\w+:\w+:\w+' #23
role24 = "(\w+)@(\w+).(\w+)"
role25 = "(\w+)@(\w+).(\w+)"

f = open('redata.txt', 'r')
for i in f:
    print re.search(role24, i).group(1)

f.close()

f=open('redata.txt', 'r')
for i in f:
    #print re.search(email, i)
    print re.sub(email, 'zekoliu@foxmail.com', i)