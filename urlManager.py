## -*- coding: utf-8 -*-
class UrlManager(object):
    # url 管理器需要维护待爬取的 url 列表 和 已爬取的 url 列表
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.newlist = set()
        self.oldlist = set()
    def add_new_url(self, url):
        if url[0] is None:
            return
        if url[0] not in self.newlist and url[0] not in self.oldlist:
            self.new_urls.add(url)
            self.newlist.add(url[0])
    # 批量添加url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断url队列中是否有内容
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获得url和解析器队列中最早一个
    def get_new_url(self):
        new_url = self.new_urls.pop()
        newl = self.newlist.pop()
        self.old_urls.add(new_url)
<<<<<<< HEAD
        self.oldlist.add(newl)
        return new_url
=======
        self.old_code.add(new_code)
        return new_url, new_code
>>>>>>> 3188c855781be6eab8bf923697ac451906fb376f
