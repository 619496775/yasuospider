# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi

class MyDoubanBookPipeline(object):
    '''
    保存到数据库中对应的class
    1.在setting.py文件中配置
    2.在自己实现的爬虫类yield item，会自动执行
    '''
    def __init__(self,dbpool):
        self.dbpool = dbpool
        
    @classmethod
    def from_settings(cls,settings):
        '''
        1.@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法
        2.类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
        3.可以通过类来调用，就像C.f()，相当于java中的静态方法
        '''
        
        #读取setting中配置的数据库参数
        dbparams = dict(
            host=settings['MYSQL_HOST'],  
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            charset='utf8mb4',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql',**dbparams)# **表示将字典扩展为关键字，相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool赋给了这个类，self中可以得到
    
    # pipeline默认调用   
    def process_item(self, item, spider):
        #重新处理content
        info = item['content'].strip().split(" / ")   #   [英] 肯·福莱特 / 于大卫 / 江苏凤凰文艺出版社 / 2016-5-1 / 129.80元
        item['price'] = info[-1]
        item['edition_year'] = info[-2]
        item['publisher'] = info[-3]
        if len(info) == 4:
            item['translator'] = info[1]
            item['author'] = info[0]
        else:
            item['translator'] = ''
            item['author'] = info[0]
        query = self.dbpool.runInteraction(self._conditional_insert,item) # 调用插入的方法
        query.addErrback(self._handle_error,item,spider) # 调用异常处理的方法
        return item
    
    # 写入数据库中
    def _conditional_insert(self,conn,item):
        sql = "insert into doubanbooks_v2(name,author,translator,publisher,edition_year,price,score,judge_people,introduce) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (item['name'],item['author'],item['translator'],item['publisher'],item['edition_year'],item['price'],item['score'],item['judge_people'],item['introduce'])
        conn.execute(sql,params)
        
    # 错误处理方法
    def _handle_error(self,failue,item,spider):
        print (failue)
