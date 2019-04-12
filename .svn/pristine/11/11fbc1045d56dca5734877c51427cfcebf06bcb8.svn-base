# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#文章类型：1: 普通文章 2. 菜谱
ARTICLE_TYPE_NORMAL = 1
ARTICLE_TYPE_RECIPE = 2


#1. 食材大类 2. 食材小类 3. 日期大类 4. 日期小类 5. 功能 6. 推荐 7. 不推荐 8. 其他（默认）
# 9.一级菜单 10.二级菜单


TAG_TYPE_1 = 1
TAG_TYPE_2 = 2
TAG_TYPE_3 = 3
TAG_TYPE_4 = 4
TAG_TYPE_5 = 5
TAG_TYPE_6 = 6
TAG_TYPE_7 = 7
TAG_TYPE_8 = 8
TAG_TYPE_9 = 9
TAG_TYPE_10= 10


class QbaobeiItem(scrapy.Item):

    name = scrapy.Field()
    type = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    image_urls =scrapy.Field()
    full_path = scrapy.Field()

class QbaobeiTag(scrapy.Item):

    tag = scrapy.Field()
    type = scrapy.Field()


