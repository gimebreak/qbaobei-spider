# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import *
from qbaobei.tools.mysql import *
from scrapy.pipelines.images import ImagesPipeline
import re
from scrapy.selector import Selector

logger = logging.getLogger(__name__)

# 文章信息入库
class QbaobeiPipeline(object):

    def process_item(self, item, spider):
        # (self, article_type, title, descriptin, material, content, source, url):
        if isinstance(item,QbaobeiItem):
            spider.db.insert_article(article_type=item['type'],title=item['name'],descriptin=item['description'],
                                   content=item['content'],url=item['url'],source=item['source'],material=None)
        return item


# tag入库
class QbaobeiTagPipeline(object):

    def open_spider(self, spider):
        spider.db = Mysql()
        spider.db.connect_db()

    def process_item(self,item,spider):

        if isinstance(item, QbaobeiTag):
            spider.db.insert_tag(item['tag'],item['type'])
            logger.info('insert tag into databases!')
        return item

# 文章标签关系入库
class QbaobeiRelPipeline(object):

    def process_item(self, item, spider):

        if isinstance(item, QbaobeiItem):
            status,art_id_data = spider.db.get_article(item['url'])
            tags = item['tags']
            print(art_id_data,"*"*200)
            for tag in tags:
                status,tag_id_data = spider.db.get_tag(tag)
                print(tag_id_data, "*" * 200)
                logger.warning("this is in QbaobeiRelPipeline %s,%s",art_id_data[0], str(tag_id_data[0]))
                try:
                    spider.db.insert_article_tag_rel(art_id_data[0], tag_id_data[0])
                except Exception as e:
                    logger.log("Error occurs inside QbaobeiRelPipeline \n %s",e)

        return item

    def close_spider(self,spider):

        spider.db.close_db()


class QbaobeiIMGPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if isinstance(item, QbaobeiItem):
            image_urls = item['image_urls']
            for url in image_urls:
                yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        if isinstance(item, QbaobeiItem):
            path = [data['path'] for ok, data in results if ok]
            logging.info("QbaobeiIMGPath[pics] : %s.", str(path))
            # 将生成的本地img path 提换 文章里的url

            content = item['content']
            res = re.findall('.*?(http.*jpg|http.*jpeg).*?', content)

            for i in range(len(res)):
                content = re.sub(res[i], path[i], content)

            item['content'] = content.strip()
            return item


