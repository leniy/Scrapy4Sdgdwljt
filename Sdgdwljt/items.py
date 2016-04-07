# -*- coding: utf-8 -*-

import scrapy

class SdgdwljtItem(scrapy.Item):
	link = scrapy.Field()
	title = scrapy.Field()
	fengongsi = scrapy.Field()
	authors = scrapy.Field()
	publishtime = scrapy.Field()
