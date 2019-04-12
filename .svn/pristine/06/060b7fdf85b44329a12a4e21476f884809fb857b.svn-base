# -*- coding: utf-8 -*-

import logging
import pymysql
import sys
from logging.handlers import RotatingFileHandler
import unicodedata
import hashlib

logger = logging.getLogger(__name__)

#控制打印到控制台
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#my_stream_handler = logging.StreamHandler(stream=sys.stdout)
#my_stream_handler.setLevel(logging.INFO)
#logger.addHandler(my_stream_handler)

#控制打印到文件
my_file_handler = RotatingFileHandler("qbaobei.log",
                                      maxBytes=1024000, backupCount=5)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
my_file_handler.setLevel(logging.INFO)
my_file_handler.setFormatter(formatter)
logger.addHandler(my_file_handler)

class Mysql(object):
    """docstring for Mysql"""
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '123456'
        self.tablename = 'qbaobei'

    #连接数据库
    def connect_db(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, db=self.tablename, port=self.port,password=self.password)
        self.cursor = self.conn.cursor()

    #关闭数据库
    def close_db(self):
        self.conn.close()
        self.cursor.close()

    #插入tag库
    def insert_tag(self, name, tag_type):

        result, id = self.get_tag(name)
        #如果数据库里不存在
        if (result == 0):
            insert_sql = "insert into jiajia_spider_tag(name, type) values (%s, %s)"
            return self.insert_data(insert_sql, (name, tag_type))

        return 0


    #获取指定tag数据
    def get_tag(self, name, tag_type=99999):
        if tag_type == 99999:
            select_sql = "select * from jiajia_spider_tag where name=%s"
            logger.info("get_tag: select * from jiajia_spider_tag where name=%s", name)
            return self.get_data(select_sql, (name))
        else:
            select_sql = "select * from jiajia_spider_tag where name=%s and type=%s"
            logger.info("get_tag: select * from jiajia_spider_tag where name=%s and type=%s", name, str(tag_type))
            return self.get_data(select_sql, (name, tag_type))

    def get_tag_by_type(self, tag_type):
        select_sql = "select * from jiajia_spider_tag where type=\'%s\'"
        return self.get_data(select_sql, (tag_type))



    #插入article库
    def insert_article(self, article_type, title, descriptin, material, content, source, url):
        result, id = self.get_article_by_title(title)
        if (result == 0):
            insert_sql = "insert into jiajia_spider_article_huaiyun(type, title, description, material, content, source, url) values(%s, %s, %s, %s, %s, %s, %s)"
            return self.insert_data(insert_sql, (article_type, title, descriptin, material, content, source, url))
        return 0

    #获取指定article数据
    def get_article(self, url):
        select_sql = "select * from jiajia_spider_article_huaiyun where url=%s"
        return self.get_data(select_sql, (url))

    #通过“标题”获取指定article数据
    def get_article_by_title(self, title):
        select_sql = "select * from jiajia_spider_article_huaiyun where title=%s"
        return self.get_data(select_sql, (title))


    #插入step库
    def insert_step(self, articleid, step, image, detail):
        result, id = self.get_step(articleid, step)
        if (result == 0):
            insert_sql = "insert into jiajia_spider_food_step(articleid, step, image, detail) values (%s, %s, %s, %s)"
            return self.insert_data(insert_sql, (articleid, step, image, detail))
        return 0

    #获取指定step数据
    def get_step(self, articleid, step):
        select_sql = "select * from jiajia_spider_food_step where articleid=%s and step=%s"
        return self.get_data(select_sql, (articleid, step))

    def get_step_by_articleid(self, articleid):
        select_sql = "select * from jiajia_spider_food_step where articleid=%s"
        return self.get_data(select_sql, (articleid))



    #插入article_tag_rel库
    def insert_article_tag_rel(self, articleid, tagid):
        result, id = self.get_article_tag_rel(articleid, tagid)

        if(result == 0):
            insert_sql = "insert into jiajia_spider_article_tag_rel(articleid, tagid) values (%s, %s)"
            return self.insert_data(insert_sql, (articleid, tagid))
        return 0

    #获取指定article_tag_rel数据
    def get_article_tag_rel(self, articleid, tagid):
        select_sql = "select * from jiajia_spider_article_tag_rel where articleid=%s and tagid=%s"
        return self.get_data(select_sql, (articleid, tagid))

    def get_article_tag_rel_by_tag_id(self, tagid):
        select_sql = "select * from jiajia_spider_article_tag_rel where tagid=%s"
        return self.get_data(select_sql, (tagid))

    def get_article_tag_rel_by_article_id(self, articleid):
        select_sql = "select * from jiajia_spider_article_tag_rel where articleid=%s"
        return self.get_data(select_sql, (articleid))


    #插入url库
    def insert_url(self, url, articleid):
        hash = self.url_md5(url)
        result, id = self.get_url(hash)
        if(result == 0):
            insert_sql = "insert into jiajia_spider_url(url, hash, articleid) values (%s, %s, %s)"
            return self.insert_data(insert_sql, (url, hash, articleid))
        return 0

    #获取指定url数据
    def get_url(self, hash):
        select_sql = "select * from jiajia_spider_url where hash=%s"
        return self.get_data(select_sql, (hash))

    def get_url_by_url(self, url):
        select_sql = "select * from jiajia_spider_url where url=%s"
        return self.get_data(select_sql, (url))


    #通用的插入库方法
    def insert_data(self, insert_sql,  values):
        logger.info("insert_data insert_sql: %s", insert_sql)
        logger.info("insert_data values: %s", values)

        try:
            result = self.cursor.execute(insert_sql, values)

        except Exception as e:
            result = 100000
            logger.error(e)
            return result

        self.conn.commit()
        return result

    #通用的获取库数据方法
    def get_data(self, select_sql, values):
        logger.info("get_data insert_sql: %s", select_sql)
        logger.info("get_data values: %s", values)

        try:
            result = self.cursor.execute(select_sql, values)
            id_data = self.cursor.fetchone()
            #logger.error("get_data result:%d, id_data:%d", result, id_data)
            return result, id_data

        except Exception as e:
            result = 100000
            logger.error(e)
            pass

    def url_md5(self, url):
        if(url != None):
            md = hashlib.md5()
            md.update(url)
            return md.hexdigest()
        else:
            return ""

if __name__ == '__main__':
    mysql = Mysql()
    mysql.connect_db()
    #mysql.insert_tag(u"测试", 1)
    #mysql.insert_article(1, u"测试", u"测试", u"测试", u"测试", u"测试")
    # mysql.insert_url("//xxx.ccc", "sgasdgdsg", 1)
    #result, id = mysql.get_url("//xxx1233.ccc")

    #result, id = mysql.get_tag(u"测试1")
    #print result, id

    #print mysql.insert_tag(u"测试3", 1)

    print mysql.get_tag(u'备孕')

    # print mysql.url_md5("//xxx1233.ccc")

    #print mysql.get_tag_by_type(1)

    # print result, id
    # mysql.insert_article_tag_rel(1,3)
    mysql.close_db()
