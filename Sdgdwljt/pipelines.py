# -*- coding: utf-8 -*-

from scrapy import signals
from scrapy.exporters import JsonItemExporter

import json
import codecs

class SdgdwljtPipeline(object):
	def __init__(self):
		self.file = codecs.open('xxoo.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

	def spider_closed(self, spider):
		self.file.close()
