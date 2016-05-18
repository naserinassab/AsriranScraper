# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from Asriran_Crawler.items import AsriranCrawlerItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

import codecs


class AsriranSpider(CrawlSpider):
    name = "asriran"
    allowed_domains = ["www.asriran.com","asriran.com"]
    start_urls = [
      "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=30&from_date=1384/01/01&to_date=1395/02/29&p=1",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=2",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=3",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=4",
      # "http://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1395/02/29&p=5",
    ]
    rules = [Rule(LinkExtractor(allow=('/fa/news/\d+/', )), callback='parse_item', follow=False)]



    def parse_item(self, response):
        item = AsriranCrawlerItem()
        item['title'] = Selector(response).xpath('//div[@class="title"]/h1/a/text()').extract()[0]
        item['body'] = ' '.join([x.strip() for x in (Selector(response).xpath('//div[@class="body"]//text()').extract())])
        item['body'] = item['body'].replace('\"','').replace("\'",'').replace(u"«","").replace(u"»","").replace(",","")
        yield item
