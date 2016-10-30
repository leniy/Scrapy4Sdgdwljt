# -*- coding:utf-8 -*-
import scrapy

from Sdgdwljt.items import SdgdwljtItem

class SdgdwljtSpider(scrapy.Spider):
	name = "sdgdwljt"
	allowed_domains = ["www.sdgdwljt.com"]

	start_urls = [
		"http://www.sdgdwljt.com/xwzx1/fgsdt/default.htm",
	]
	for i in range(1,50):
		# 网站上只保留50个静态列表页面
		start_urls.append("http://www.sdgdwljt.com/xwzx1/fgsdt/default_" + str(i) + ".htm")
	start_urls.append("http://www.sdgdwljt.com/xwzx1/jtyw/default.htm")
	for i in range(1,25):
		# 网站上只保留25个静态列表页面
		start_urls.append("http://www.sdgdwljt.com/xwzx1/jtyw/default_" + str(i) + ".htm")

	def parse(self, response):
		for selects in response.xpath('//div[@id="layout"]/div/div/ul/li'):
			link = selects.xpath('a/@href').extract()[0] # 相对地址
			link = response.urljoin(link) # 绝对地址
			yield scrapy.Request(link, callback=self.parse_contents)

	def parse_contents(self, response):
		item = SdgdwljtItem()
		item['link']        = response.url
		item['title']       = response.xpath('//div[@id="top"]/h1/text()').extract()[0]
		item['fengongsi']   = response.xpath('//div[@id="top"]/p/span[1]/text()').extract()[0]
		item['authors']     = response.xpath('//div[@id="top"]/p/span[2]/text()').extract()[0]
		item['publishtime'] = response.xpath('//div[@id="top"]/p/span[3]/text()').extract()[0]
		yield item
