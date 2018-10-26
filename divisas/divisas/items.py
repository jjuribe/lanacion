# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DivisasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nombre = scrapy.Field()
    ultimo = scrapy.Field()
    anterior = scrapy.Field()
    variacion = scrapy.Field()
    fechahora = scrapy.Field(serializer=str)
    pass
