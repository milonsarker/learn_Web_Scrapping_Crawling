import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self, response):
		quotes = response.xpath('//*[@class = "quote"]')
		for qt in quotes: 
			text = qt.xpath('.//*[@class = "text"]/text()').extract_first()
			author = qt.xpath('.//*[@class = "author"]/text()').extract_first()
			tags = qt.xpath('.//*[@itemprop = "keywords"]/@content').extract_first()
			print("----------------------------------------------------------------------------")
			print(text + "\n" + author + "\n" + str(tags))
			print("----------------------------------------------------------------------------")
