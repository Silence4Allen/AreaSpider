# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from AreaSpider.settings import SQL_DATETIME_FORMAT


class AreaspiderItem(scrapy.Item):
    # province, city, cityCode, county, countyCode, town, townCode, village, villageType,villageCode
    crawl_time = scrapy.Field()
    crawl_update_time = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    cityCode = scrapy.Field()
    county = scrapy.Field()
    countyCode = scrapy.Field()
    town = scrapy.Field()
    townCode = scrapy.Field()
    village = scrapy.Field()
    villageCode = scrapy.Field()
    villageType = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
        insert into area(crawl_time, crawl_update_time, province, city, cityCode, county, 
        countyCode, town, townCode, village, villageCode, villageType)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        crawl_time=VALUES(crawl_time),
        crawl_update_time=VALUES(crawl_update_time)
        """

        params = (self['crawl_time'].strftime(SQL_DATETIME_FORMAT),
                  self['crawl_update_time'].strftime(SQL_DATETIME_FORMAT),
                  self['province'],
                  self['city'],
                  self['cityCode'],
                  self['county'],
                  self['countyCode'],
                  self['town'],
                  self['townCode'],
                  self['village'],
                  self['villageCode'],
                  self['villageType'])
        return insert_sql, params
