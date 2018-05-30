# -*- coding: utf-8 -*-
import scrapy


class TabnakSpiderSpider(scrapy.Spider):
    name = 'tabnak_spider'
    allowed_domains = ['www.tabnak.ir']
    start_urls = ['http://www.tabnak.ir/']

    def parse(self, response):
        pass
