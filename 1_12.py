
import re
k = 'bat|bit|but|hat|hit|hut'
# print re.match(k, 'bat hit').group() #1

name = r'\w+\s\w+'
realname = re.match(name, 'kobe bryant')
# print realname.group() #2

name1 = '\w+,\s\w+'
realname1 = re.match(name1, 'kobe, bryant')
# print realname1.group() #3

pattren = r'/b[a-zA-Z_](\w|_)*\b' #4

address = '\d+\s(\w+\s)*\w+' #5
# print re.match(address, '1102 Bordeaux ko nr ko Drive').group()

netaddress = '^www.(.)*(.com|.net|.edu)' #6
# print re.match(netaddress, 'www.ucsc.net').group()

role7 = '\d+'       #7
role8 = '\d+[L]?'   #8
role9 = '\d+.\d+'   #9
role10 = '\d'       #10

emailadd = "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
           #'\w+@.\w+.com' #11
print re.match(emailadd, 'zekoli@gmail.com').group()

webaddr = 'www.\w+(.com|.edu|.net)' #12
print re.match(webaddr, 'www.google.com').group()