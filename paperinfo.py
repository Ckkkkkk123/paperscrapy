'''
抓取论文的名称，链接，作者
https://dblp.uni-trier.de/db/journals?pos=01
最大4501项
python版本： 3.7
os: macos
'''
import requests
import os
import queue
from bs4 import BeautifulSoup
# 用一个队列保存url
q = queue.Queue()
# 首页我们写好抓取网页的函数
def get_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }
        r = requests.get(url=url, headers=headers)
        r.encoding = 'utf-8'
        content = r.text
        return content
    except:
        s = sys.exc_info()
        print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        return " ERROR " 
# 解析内容
def praseContent(content):
    soup = BeautifulSoup(content,'html.parser')
    trasplist = soup.find_all('li',class_="entry article")
    for item in trasplist:
       paperurl = item.find('div',class_='head').a.get('href')
       articleinfo = item.find('article',class_="data").find_all('span')
       title = item.find('span',class_='title').text
       articleinfo.pop()
       articleinfo.pop()
       authors = ""
       for author in articleinfo:
           authors = authors + author.text+";"
       print(authors,title,paperurl)
url = "https://dblp.uni-trier.de/db/journals/taccess/taccess8.html"
content = get_content(url)
praseContent(content)