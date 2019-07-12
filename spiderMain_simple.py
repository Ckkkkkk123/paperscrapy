## -*- coding: utf-8 -*-
import htmlDownloader
import htmlParser
import urlManager
import gevent
class SpiderMain(object):
    # 爬虫总调度程序会使用 url 管理器、 html 的下载器、解析器、输出器，下面初始化一下：
    def __init__(self):
        self.download = htmlDownloader.HtmlDownloader()
        self.urls = urlManager.UrlManager()
        self.parser = htmlParser.HtmlParser()
    # 保存数据到txt
    def save(self,title,authors,url):
        print('save')
    # craw方法,爬虫调度程序
    def craw(self,root_url):
        # 添加入口url到urlmanager中
        self.urls.add_new_url((root_url,0))
        # 启动爬虫循环
        while self.urls.has_new_url():
            new_urls = set()
            while self.urls.has_new_url():
            # 当 url 管理器里待爬取的 url 时，获取一个 url
                new_urls.add(self.urls.get_new_url())
            # 进入解析器进行解析。
            gevent.joinall([gevent.spawn(self.process,new_url) for new_url in new_urls])
    def process(self,new_url):
        # 启动下载器
        print('begin download')
        html_content = self.download.download(new_url[0])
        print(new_url[0])
        # 进入解析器进行解析。
        if new_url[1] == 0:
            urls = self.parser.parseEntry(html_content)
            self.urls.add_new_urls(urls)
        elif new_url[1] == 1:
            urls1 = self.parser.parseStran(html_content)
            self.urls.add_new_urls(urls1)
        elif new_url[1] == 2:
            title,authors,paperurl = self.parser.parsePaper(html_content)
            if title != 0:
                self.save(title,authors,paperurl)

if __name__ == "__main__":
    root_url = "https://dblp.uni-trier.de/db/journals?pos=01"
    obj_spider = SpiderMain()
    # obj_spider.craw(root_url)
    
