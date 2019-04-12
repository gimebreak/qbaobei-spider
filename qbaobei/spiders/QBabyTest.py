# -*- coding: utf-8 -*-
import scrapy
from qbaobei.items import *
from scrapy import Request
from copy import deepcopy
from qbaobei.tools.mysql import *
from qbaobei.tools import utils
import requests
from lxml import etree
import re



class QbabytestSpider(scrapy.Spider):
    name = 'QBabyTest'
    allowed_domains = ['qbaobei.com']
    # start_urls = ['http://www.qbaobei.com/jiankang/huaiyun/',
    #               'http://www.qbaobei.com/jiankang/fenmian/',
    #               'http://www.qbaobei.com/jiankang/chanhou/']
    start_urls = ['http://www.qbaobei.com/jiankang/fenmian/']

    # 调取菜单
    def parse(self, response):
        menu_url = response.xpath("//div[@class='second-nav']/a/@href").extract()[1:]
        menu_name = response.xpath("//div[@class='second-nav']/a/text()").extract()[1:]
        navi_name = response.xpath('//li[@class="active"]/a/text()').extract_first()
        navi_url = response.xpath('//li[@class="active"]/a/@href').extract_first()
        tagitem = QbaobeiTag()

        # 一级目录名
        for item in navi_name:
            tagitem['tag'] = item
            tagitem['type'] = TAG_TYPE_9
            yield tagitem

        # 二级目录名
        for item in menu_name:
            tagitem['tag'] = item
            tagitem['type'] = TAG_TYPE_10
            yield tagitem

        menu = zip(menu_name, menu_url)
        for name,url in menu:
            yield Request(url=url, callback=self.list_parse,
                          meta={"menu_name": name, "nav_name": navi_name})  #可以更改navi_name

    # 遍历页面
    def list_parse(self, response):
        current_url = response.url
        menu_tag = response.meta['menu_name']
        nav_tag = response.meta['nav_name']
        end_page = int(response.xpath('//div[@class="page"]/a[@class="end"]/text()').re('...(\d*)')[0])

        for i in range(1, 1+end_page):    # iterator limits
            next_url = current_url + 'List_{}.html'.format(i)
            print(next_url)
            yield Request(next_url,callback=self.article_parse, meta={"menu_name": menu_tag,"nav_name": nav_tag})

    # 解析文章信息
    def article_parse(self, response):
        menu_tag = response.meta['menu_name']
        nav_tag = response.meta['nav_name']
        db = Mysql()
        db.connect_db()
        title_url = response.xpath('//ul[@class="list-conBox-ul"]/li/a/@href').extract()
        title = response.xpath('//ul[@class="list-conBox-ul"]/li/div/a/text()').extract()
        title_desc = response.xpath('//p[@class="info"]').extract()
        # 取单页文章节点
        title_node = response.xpath('//ul[@class="list-conBox-ul"]/li')
        # 一篇文章的tag
        title_tag = title_node.xpath('div//span[@class="tipsm"]/a/text()').extract()
        # 所有文章tag
        class_tag = map(lambda x: x.xpath('div//span[@class="tipsm"]/a/text()').extract(), title_node)
        # 去重tag
        DR_tag = reduce(lambda x, y: list(set(x + y)), class_tag)
        tagitem = QbaobeiTag()

        for tag in DR_tag:
            tagitem['tag'] = tag
            tagitem['type'] = 8
            logger.warning('this is to print TAG')
            yield tagitem

    # pass info to pipeline
        for index in range(len(title_url)):
            #
            # if self.db.get_data('select url from jiajia_spider_article where url = %s',
            #                                         (title_url[index]))[0] == 1:
            #     continue
            item = QbaobeiItem()
            item['name'] = title[index]
            item['type'] = ARTICLE_TYPE_NORMAL
            item['description'] = title_desc[index]
            item['url'] = title_url[index]
            item['source'] = u'亲亲宝贝'
            item['tags'] = class_tag[index] + [menu_tag, nav_tag]

            yield Request(title_url[index], callback=self.content_parse, meta={'baobeiitem': deepcopy(item)})

    # 获取文章内容及图片
    def content_parse(self, response):
        item = response.meta["baobeiitem"]

        # 有内容分页
        if response.xpath('//div[@class="detail_page"]/a/@href').extract():
            page_urls = response.xpath('//div[@class="detail_page"]/a/@href').extract()
            correction_urls = utils.add_prefix(response,page_urls)
            content_text,img_urls = self.get_content(correction_urls)
            item['content'] = content_text
            item['image_urls'] = img_urls
            yield item

        # 没有分页
        content_text, img_urls = self.text_parse(response)
        item['content'] = content_text
        item['image_urls'] = img_urls

        yield item

    def text_parse(self, response):
        # 无步骤
        html_type_one = response.xpath('//div[@class="detail-area"]')

        # 有步骤
        html_type_two = response.xpath('//div[@class="detail-area baike-detail"]')

        content_html = html_type_one if html_type_one else html_type_two
        image_urls = response.xpath('//div[starts-with(@class,"detail-area")]//img/@src').extract()

        content_html = content_html.extract_first()
        content_text = re.sub('(<\/?a.*?>)', '', content_html)

        return content_text, image_urls


    def get_content(self,urls):

        total_image_urls = []
        total_content = ''

        # 还要增加无图片情况   http://www.qbaobei.com/jiankang/beiyun/201187-25224.html
        for url in urls:
            temp = requests.get(url)
            xml = etree.HTML(temp.content)

            html_content = etree.tostring(xml.xpath('//div[starts-with(@class,"detail-area")]')[0])  #有图片or 无图片
            html_content = re.sub('<\/?div.?page\">.\/div>','',html_content)
            total_content += html_content
            image_urls = xml.xpath('//div[starts-with(@class,"detail-area")]//img/@src')

            total_image_urls += image_urls

            # content_text = re.sub('\s+(12)\s+ | \s+(23)\s+ ', '  ', total_content) # 要去标签

        return total_content, total_image_urls
