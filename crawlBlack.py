
import requests
from lxml import etree
import pandas as pd
import time
import random
from tqdm import tqdm

name, score, comment = [], [], []

def danye_crawl(page):
   url = 'https://movie.douban.com/subject/6390825/comments?start=%s&limit=20&sort=new_score&status=P&percent_type='%(page*20)
   response = requests.get(url)
   response = etree.HTML(response.content.decode('utf-8'))
   if requests.get(url).status_code == 200:
       print('\n', '第%s页评论爬取成功'%(page))
   else:
       print('\n', '第%s页爬取失败'(page))

   for i in range(1,21):
       name_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/a'%(i))
       score_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]'%(i))
       comment_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/p'%(i))

       name_element = name_list[0].text
       score_element = score_list[0].attrib['class'][7]
       comment_element = comment_list[0].text

       name.append(name_element)
       score.append(score_element)
       comment.append(comment_element)

for i in tqdm(range(11)):
   danye_crawl(i)
   time.sleep(random.uniform(6, 9))

res = {'name':name, 'score':score, 'comment':comment}
res = pd.DataFrame(res, columns = ['name','score','comment'])
res.to_csv("豆瓣.csv", encoding='utf-8-sig')