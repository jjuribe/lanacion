# -*- coding: utf-8 -*-
import scrapy
from divisas.items import *


class LanacionSpider(scrapy.Spider):
    name = 'lanacion'
    allowed_domains = ['lanacion.com.ar']
    start_urls = ['http://www.lanacion.com.ar/economia/divisas']

    def parse(self, response):
        ##print(response.xpath('//*[@id="acumulado"]/section[3]/section[1]/div/div/div').extract())
        divisas = response.xpath('//*[@id="acumulado"]/section[3]/section[1]/div/div/div')

        items = []

        for divisa in divisas:
            item = DivisasItem()
            print (divisa.xpath('label[1]').extract())
            item['nombre']  = divisa.xpath('label[1]/text()').extract()
            item['ultimo'] = divisa.xpath('label[2]/b/text()').extract()
            item['anterior'] = divisa.xpath('label[3]/text()').extract()
            item['variacion'] = divisa.xpath('label[4]/text()').extract()
            item['fechahora'] = divisa.xpath('label[5]/text()').extract()

            items.append(item)


        ##pass

        return items

