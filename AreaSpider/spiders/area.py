# # -*- coding: utf-8 -*-
# import datetime
# from urllib import parse
#
# import scrapy
# from scrapy.http import Request
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
#
# from AreaSpider.items import AreaspiderItem
#
#
# class AreaSpider(CrawlSpider):
#     name = 'area'
#     allowed_domains = ['www.stats.gov.cn']
#     start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html']
#
#     rules = (
#         Rule(LinkExtractor(allow=r'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/\d+'),
#              callback='parse_province', follow=True),
#     )
#
#     def parse_start_url(self, response):
#         provinceInfos = response.css('tr[class="provincetr"] td a')
#         for provinceInfo in provinceInfos:
#             province = provinceInfo.css('::text').extract_first()
#             provinceUrl = provinceInfo.css('::attr(href)').extract_first()
#             yield Request(url=parse.urljoin(response.url, provinceUrl), meta={"province": province},
#                           callback=self.parse_province)
#
#     # province,city,cityCode,county,countyCode,town,townCode,village,villageCode
#     def parse_province(self, response):
#         cityInfos = response.css('tr[class="citytr"]')
#         for cityInfo in cityInfos:
#             cityCode = cityInfo.css('a::text').extract_first()
#             city = cityInfo.css('a::text')[1].extract()
#             cityUrl = cityInfo.css('a::attr(href)').extract_first()
#             yield Request(url=parse.urljoin(response.url, cityUrl),
#                           meta=dict({'cityCode': cityCode, 'city': city}, **response.meta),
#                           callback=self.parse_city)
#
#     def parse_city(self, response):
#         countyInfos = response.css('tr[class="countytr"]')
#         for countyInfo in countyInfos:
#             countyInfoContent = countyInfo.css('td')
#             countyCode = countyInfoContent.css('::text').extract_first()
#             county = countyInfoContent.css('::text')[1].extract()
#             countyUrl = countyInfoContent.css('a::attr(href)').extract_first()
#             if countyUrl != None:
#                 yield Request(url=parse.urljoin(response.url, countyUrl),
#                               meta=dict({'countyCode': countyCode, 'county': county}, **response.meta),
#                               callback=self.parse_county)
#
#     def parse_county(self, response):
#         townInfos = response.css('tr[class="towntr"]')
#         for townInfo in townInfos:
#             townCode = townInfo.css('a::text').extract_first()
#             town = townInfo.css('a::text')[1].extract()
#             townUrl = townInfo.css('a::attr(href)').extract_first()
#             yield Request(url=parse.urljoin(response.url, townUrl),
#                           meta=dict({'townCode': townCode, 'town': town}, **response.meta),
#                           callback=self.parse_town)
#
#     def parse_town(self, response):
#         villageInfos = response.css('tr[class="villagetr"]')
#         for villageInfo in villageInfos:
#             item = AreaspiderItem()
#             item['villageCode'] = villageInfo.css('td::text').extract_first()
#             item['villageType'] = villageInfo.css('td::text')[1].extract()
#             item['village'] = villageInfo.css('td::text')[2].extract()
#             item['province'] = response.meta['province']
#             item['city'] = response.meta['city']
#             item['cityCode'] = response.meta['cityCode']
#             item['county'] = response.meta['county']
#             item['countyCode'] = response.meta['countyCode']
#             item['town'] = response.meta['town']
#             item['townCode'] = response.meta['townCode']
#             item['crawl_time'] = datetime.datetime.now()
#             item['crawl_update_time'] = datetime.datetime.now()
#             yield item
