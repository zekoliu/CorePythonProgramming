
import re
import urllib.request

def getlink(url):
    headers = ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.add_handlers = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link

url = 'http://blog.csdn.net/'
linklist = getlink(url)
for link in linklist:
    print(link)