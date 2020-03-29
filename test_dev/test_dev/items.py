# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PycoderItem(scrapy.Item):
    timestamp = scrapy.Field()
    RPC = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    marketing_tags = scrapy.Field()  # list of str
    brand = scrapy.Field()
    section = scrapy.Field()  # list str
    price_data = scrapy.Field()   # nested dict
    stock = scrapy.Field()   # nested dict
    assets = scrapy.Field()   # nested dict
    metadata = scrapy.Field()   # nested dict
