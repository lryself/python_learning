# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from items import MainSpiderItem
from config import job_URL


class A51jobSpider(scrapy.Spider):
    name = '51job'
    start_urls = [job_URL]
    error_count = 0

    def parse(self, response):
        next_page = response.xpath('//a[text()="下一页"]/@href').extract_first()
        # 获取下一页url
        if next_page:
            yield Request(url=next_page, callback=self.parse, dont_filter=True)

        all_job = response.xpath('//div[@id="resultList"]//div[@class="el"]')
        for i in all_job:
            yield self.parse_onejob(i)

    def parse_onejob(self, text):
        '''
        爬取单个职位信息
        :param text: xpath类型数据
        :return:
        '''
        item = MainSpiderItem()
        item["name"] = ''
        item["company"] = ''
        item["site"] = ''
        item["salary"] = ''
        item["date"] = ''
        try:
            name = text.xpath('./p/span/a/@title').extract()[0]
            company = text.xpath('./span[1]/a/@title').extract()[0]
            site = text.xpath('./span[2]/text()').extract()[0]
            salary = text.xpath('./span[3]/text()').extract()[0]
            date = text.xpath('./span[4]/text()').extract()[0]
            item["name"] = name.split()[0]
            item["company"] = company
            item["site"] = site
            item["salary"] = salary
            item["date"] = date
        except IndexError:
            self.error_count += 1
            print("有{}个职位信息不全".format(self.error_count))
        return item
