#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from fetchman.pipeline.base_pipeline import ItemPipeline
from database.fa_paper import MYSQL
from fetchman.utils import FetchManLogger
import traceback
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')
dbconn = MYSQL(
        dbhost = 'localhost', 
        dbuser = 'root', 
        dbpwd = 'goodlife1', 
        dbname = 'paper', 
        dbcharset = 'utf8')

# 表结构
# title = Column(String(100), primary_key=True)
# paperFrom = Column(String(100))
# catory = Column(String(200))
# authors = Column(String(200))
# paperUrl = Column(String(200))
# 存入数据库pipeline
class DataBasePipeline(ItemPipeline):
    def process_item(self, item):
        try:
            dbconn.insert(table='paper_skam', data=item)
        except Exception:
            FetchManLogger.logger.error(traceback.format_exc())