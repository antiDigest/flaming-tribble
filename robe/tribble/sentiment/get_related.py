from scrapy import Selector
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from senti import *
from tribble.models import Words_India, Words_Global

class MakeSpider(Spider):
    name = 'runspider'
    allowed_domains = ['twitter.com']
    start_urls = []
    country = ''

    def __init__(self, url='', country=''):
    	self.start_urls = [url]
    	self.country= country

    def parse(self, response):
	    if self.country == 'India':
	    	statement = []
	    	i=0
	        for titles in response.xpath('//div[@class="content"]'):
	        	i+=1
	        	statement += titles.xpath('p/text()').extract()
	        	if i>20:
	        		break
	        max_value, max_senti = getSenti(statement)
	        print max_value, max_senti, response
	    else:
	    	statement = []
	    	i=0
	        for titles in response.xpath('//div[@class="content"]'):
	        	i+=1
	        	statement += titles.xpath('p/text()').extract()
	        	if i>20:
	        		break
	        max_value, max_senti = getSenti(statement)
	        print max_value, max_senti