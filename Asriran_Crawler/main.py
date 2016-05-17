from scrapy import cmdline
cmdline.execute("scrapy crawl asriran -o news.csv -t csv".split())
# cmdline.execute("scrapy crawl test -o items.csv -t csv".split())