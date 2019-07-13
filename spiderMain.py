#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fetchman.spider.spider_core import SpiderCore
from fetchman.processor.base_processor import BaseProcessor
from fetchman.downloader.http.spider_request import Request
from fetchman.utils.decorator import check
from pipelines.console_pipeline import ConsolePipeline
from pipelines.database_pipeline import DataBasePipeline
from fetchman.pipeline.pipe_item import pipeItem
from bs4 import BeautifulSoup
import hashlib
import time
import random
import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')

class Zhu_Processor(BaseProcessor):
    spider_id = 'zhu_spider'
    allowed_domains = ['doi.org','dblp.uni-trier.de']
    start_requests = [Request(url='https://dblp.uni-trier.de/db/journals?pos=01', priority=0)]

    @classmethod
    def init_start_requests(cls):
        cls.start_requests.extend([Request(url='https://dblp.uni-trier.de/db/journals?pos=%d' % page,callback=self.process_entry, priority=0,duplicate_remove=False) for page in range(1,4500)])
    
    @check
    def process(self,response):
        soup = BeautifulSoup(response.m_response.content,'html.parser')
        link = soup.find(name='div',class_='hide-body').find_all('a')
        for ref in link:
            stranurl = ref.get('href')
            request = Request(url=stranurl, priority=1, callback=self.process_stran)
            yield request

    @check
    def process_stran(self,response):
        soup = BeautifulSoup(response.m_response.content, 'html.parser')
        link = soup.select('#main')[0]
        ullink = ""
        for item in link.children:
            if item.name == 'ul':
                ullink = item
        infolist = ullink.find_all('a')
        for temp in infolist:
            paperlink = temp.get('href')
            request = Request(url=paperlink, priority=1, callback=self.process_paper)
            request.meta['paperFrom'] = paperlink
            yield request
    
    @check
    def process_paper(self,response):
        soup = BeautifulSoup(response.m_response.content, 'html.parser')
        catory = soup.find('header').text.split(',')[0]
        # paperFrom = response.request.meta['paperFrom']
        trasplist = soup.find_all('li', class_="entry article")
        articleinfo = []
        for item in trasplist:
            atag = item.find('div',class_='head').find('a')
            if atag is None:
                return 0,0,0
            paperurl = atag.get('href')
            articleinfo = item.find('article', class_="data").find_all('span')
            title = item.find('span', class_='title').text
            articleinfo.pop()
            articleinfo.pop()
            authors = ""
            for author in articleinfo:
                authors = authors + author.text + ";"
            result = dict()
            result['title'] = title
            result['authors'] = authors
            result['paperUrl'] = paperurl
            result['catory'] = catory
            # result['paperFrom'] = paperFrom
            yield pipeItem(['console','database'],result)
if __name__ == '__main__':
    SpiderCore(Zhu_Processor()) \
        .set_pipeline(ConsolePipeline(), 'console') \
        .set_pipeline(DataBasePipeline(), 'database') \
        .start()
