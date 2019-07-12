## -*- coding: utf-8 -*-
import htmlDownloader
import htmlParser
import urlManager

class SpiderMain(object):
    # 爬虫总调度程序会使用 url 管理器、 html 的下载器、解析器、输出器，下面初始化一下：
    def __init__(self):
        self.download = htmlDownloader.HtmlDownloader()
        self.urls = urlManager.UrlManager()
        self.parser = htmlParser.HtmlParser()
    
    # craw方法,爬虫调度程序
    def craw(self,root_url):
        count = 1
        # 添加入口url到urlmanager中
        self.urls.add_new_url(root_url, 0)
        # 启动爬虫循环
        while self.urls.has_new_url():
            try:
                # 当 url 管理器里待爬取的 url 时，获取一个 url
                new_url,new_code = self.urls.get_new_url()
                print(new_code,new_url)
                # 启动下载器并存储
                # html_content = self.download.download(new_url)
                # 进入解析器进行解析。此处需要编入编码用来识别解析器选择哪一个
            
            except Expect as error:
                print('crew faild:')


if __name__ == "__main__":
    root_url = "https://dblp.uni-trier.de/db/journals?pos=01"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) # 启动爬虫