
import re
import urllib.request

def craw(url, page):
    html = urllib.request.urlopen(url).read()
    html1 = str(html)
    # < img
    # src = "//img11.360buyimg.com/popshop/jfs/t5662/36/8888655583/7806/1c629c01/598033b4Nd6055897.jpg"
    # width = "102"
    # height = "36"
    pat2 = '<img src="//(.+?\.jpg)" width="102" height="36"'
    print(pat2)
    imagelist = re.compile(pat2).findall(html1)
    x = 1
    for imageurl in imagelist:
        print((imageurl))
        imagename = '/home/jenenliu/Desktop/crawel/' + str(page) + str(x) + '.jpg'
        imageurl = 'http://' + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x+=1
            if hasattr(e, "reason"):
                x+=1

for i in range(1, 70):
    url = 'https://coll.jd.com/list.html?sub=23289&page=' + str(i)
    craw(url, i)