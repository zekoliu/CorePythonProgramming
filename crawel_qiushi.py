
import re
import urllib.request

def getcontent(url, page):
    headers = ('Usger-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    datatemp = urllib.request.urlopen(url)
    data = datatemp.read().decode('utf-8')
    userpat = 'taget="_black" title="(.*?)">'
    contentpat = '<div class="content">(.*?)</div>'
    userlist = re.compile(userpat, re.S).findall(data)
    contentlist = re.compile(contentpat, re.S).findall(data)
    x = 1
    for content in contentlist:
        content = content.replace("\n", '')
        name = 'content' + str(x)
        exec(name+'=content')
        x+=1

    y = 1
    for user in userlist:
        name = 'content' + str(y)
        print(' 用户 ' + str(page) + str(y) + ' 是: ' + user)
        print(" 内容是： ")
        exec('print(' + name + ')')
        print('\n')
        y+=1

for i in range(1, 30):
    url = 'https://www.qiushibaike.com/text/page/' + str(i)
    getcontent(url, i)