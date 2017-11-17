import scrapy
from myfirstcrawler.items import BlogItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class Mycrawler(CrawlSpider):
	name = "test_scraper"

	allowed_domains = ["www.analyticsvidhya.com"]
	# First Start Url
	start_urls = ["https://www.analyticsvidhya.com/blog/"]

	custom_settings = {
    # specifies exported fields and order
    'FEED_EXPORT_FIELDS': ["Fromurl", "Tourl"],
	}
	
	rules = [Rule(LinkExtractor(canonicalize=True,unique=True), callback="parse_items")]
	
	npages = 2

	# This mimics getting the pages using the next button. 
	for i in range(2, npages + 198):
		start_urls.append("https://www.analyticsvidhya.com/blog/page/"+str(i)+"/")
	
	def parse_items(self, response):
		#item = TechcrunchItem()
		items = []
		links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
		for link in links:
			for domain in self.allowed_domains:
				if domain in link.url:
					item = BlogItem()
					item['Fromurl'] = response.url
					item['Tourl'] = link.url
					url = link.url
					items.append(item)
		return(items)

