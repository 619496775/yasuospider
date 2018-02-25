# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyDoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()           #名称
    content = scrapy.Field()        #第二栏
    score = scrapy.Field()          #评分
    judge_people = scrapy.Field()   #评价人数
    introduce = scrapy.Field()      #介绍
    price = scrapy.Field()          #价格
    edition_year = scrapy.Field()   #出版日期
    publisher = scrapy.Field()      #出版社
    translator = scrapy.Field()     #译者
    author = scrapy.Field()         #作者
    