'''
为解析器中的GET请求添加头部
'''

# -*- coding: utf-8 -*-
import requests
import sys


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        try:
            headers = {
                'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            }

            r = requests.get(url=url, headers=headers)
            r.encoding = 'utf-8'
            content = r.text
            return content
        except:
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
            return " ERROR "
