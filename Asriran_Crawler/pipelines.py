# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AsriranCrawlerPipeline(object):
    def process_item(self, item, spider):
        f= open(r"C:\OneDrive\Projects\Asriran_Crawler\news.csv","a")
        f.writable("%s,%s\n" % (item.title,item.body))
        f.close()
        return item
