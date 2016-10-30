# -*- coding: utf-8 -*-

import sqlite3
from scrapy import signals
from scrapy.exporters import JsonItemExporter

import json
import codecs

class SdgdwljtPipeline(object):
	def __init__(self):
		self.conn = sqlite3.connect('test.db')
		self.conn.execute('''CREATE TABLE IF NOT EXISTS urllist (link TEXT NOT NULL UNIQUE, title TEXT NOT NULL, fengongsi TEXT NOT NULL, authors TEXT NOT NULL, publishtime TEXT NOT NULL);''')

	def process_item(self, item, spider):
		self.conn.execute("REPLACE INTO urllist (link, title, fengongsi, authors, publishtime) VALUES ('%s','%s','%s','%s','%s')" % (item['link'],item['title'],item['fengongsi'],item['authors'],item['publishtime']))
		self.conn.commit()
		return item

	def spider_closed(self, spider):
		self.conn.close()
