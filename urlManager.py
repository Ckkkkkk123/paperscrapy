## -*- coding: utf-8 -*-
class UrlManager(object):
# url 管理器需要维护待爬取的 url 列表 和 已爬取的 url 列表
    def __init__(self):
        self.new_urls = set()
        self.new_code = set()
        self.old_urls = set()
        self.old_code = set()

    def add_new_url(self, url,code):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            self.new_code.add(code)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        new_code = self.new_code.pop()
        self.old_urls.add(new_url)
        self.old_code.add(new_code)
        return new_url,new_code