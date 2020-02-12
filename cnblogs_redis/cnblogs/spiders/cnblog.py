# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy_redis.spiders import RedisSpider
class CnblogSpider(RedisSpider):
    name = 'cnblog'
    redis_key = "myspider:start_urls"
    #start_urls = [f'https://www.cnblogs.com/c-x-a/default.html?page={i}' for i in range(1,2)]
    
    def parse(self, response):
        main_info_list_node = response.xpath('//div[@class="forFlow"]')
        content_list_node = main_info_list_node.xpath(".//a[@class='postTitle2']/text()").extract()
        for item in content_list_node:
            url = response.url
            title=item
            crawl_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item = {}
            item['url'] = url
            item['title'] = title.strip() if title else title
            item['crawl_date'] = crawl_date
            yield item

