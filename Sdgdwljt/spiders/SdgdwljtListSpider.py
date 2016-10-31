# -*- coding: utf-8 -*-
import scrapy


class SdgdwljtlistspiderSpider(scrapy.Spider):
    name = "SdgdwljtListSpider"
    allowed_domains = ["www.sdgdwljt.com"]
    start_urls = ['http://www.sdgdwljt.com/']

    def parse(self, response):
        pass
