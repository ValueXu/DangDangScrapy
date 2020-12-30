# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class Ddspider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ('http://www.dangdang.com/',)
    def parse(self, response):
        item=DangdangItem()
        item["title"]=response.xpath("//a[@class='pic']/@title").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        item["price"]=response.xpath("//p[@class='price']/span[@class='search_now_price']/text()").extract()
        yield item
        for i in range(2,101):
            url="http://category.dangdang.com/pg" +str(i)+"-cp01.54.06.00.00.00.html"
            yield Request(url,callback=self.parse)