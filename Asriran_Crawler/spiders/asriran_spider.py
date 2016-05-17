# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import Rule, CrawlSpider
import re
from Asriran_Crawler.items import AsriranCrawlerItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class AsriranSpider(CrawlSpider):
    name = "asriran"
    allowed_domains = ["asriran.com"]
    start_urls = (
        'http://www.asriran.com/fa/archive',
    )
    #rules = (Rule(SgmlLinkExtractor(allow=[r'fa/news/\d+']), callback='parse', follow=True),)

    def parse(self, response):
        title = response.xpath('//*[@class="title"]/text()').extract()
        title = ' '.join(title)
        body = response.xpath('//*[@class="body"]/text()').extract()
        body = ' '.join(body)
        item = AsriranCrawlerItem(title=title,
          body=body)
        return item
