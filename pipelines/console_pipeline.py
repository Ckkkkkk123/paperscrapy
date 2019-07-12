#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from fetchman.pipeline.base_pipeline import ItemPipeline
from fetchman.utils import FetchManLogger
import traceback

# 输出pipeline
class ConsolePipeline(ItemPipeline):
    def process_item(self, item):
        try:
            print(item)
        except:
            FetchManLogger.logger.error(traceback.format_exc())
