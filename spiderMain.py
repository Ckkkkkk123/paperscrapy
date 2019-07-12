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
        # 添加入口url到urlmanager中
        self.urls.add_new_url((root_url,0))
        # 启动爬虫循环
        while self.urls.has_new_url():
            try:
                # 当 url 管理器里待爬取的 url 时，获取一个 url
                new_url = self.urls.get_new_url()
                print(new_url)
                # 启动下载器
                html_content = self.download.download(new_url[0])
                # 进入解析器进行解析。此处需要编入编码用来识别解析器选择哪一个
                if new_url[1] == 0:
                    print('使用了入口解析器')
                    urls = self.parser.parseEntry(html_content)
                    self.urls.add_new_urls(urls)
                elif new_url[1] == 1:
                    print('使用了解析器1号')
                    urls1 = self.parser.parseStran(html_content)
                    self.urls.add_new_urls(urls1)
                elif new_url[1] == 2:
                    print('是用来解析器2号')
                    self.parser.parsePaper(html_content)
            except:
                print('crew faild:')


if __name__ == "__main__":
    root_url = "https://dblp.uni-trier.de/db/journals?pos=01"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫
