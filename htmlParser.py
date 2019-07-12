# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class HtmlParser(object):
    # 解析器编号0
    def parseEntry(self, content):
        soup = BeautifulSoup(content,'html.parser')
        link = soup.find(name='div',class_='hide-body').find_all('a')
        for ref in link:
            print(ref.text,ref.get('href'))
    # 解析器编号1
    def parseStran(self,content):
        soup = BeautifulSoup(content,'html.parser')
        link = soup.select('#main')[0]
        ullink = ""
        for item in link.children:
            if item.name == 'ul':
                ullink = item
        infolist = ullink.find_all('a')
        for temp in infolist:
            print(temp.text,temp.get('href'))
    # 解析器编号2
    def parsePaper(self,content):
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
