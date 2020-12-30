# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import os

class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="dangdangbook")
        cursor = conn.cursor()
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            price=item["price"][i]
            print(title)
            #print(link)
            #print(comment)
            print(price)
            sql="insert into dddata(title,url,comment,price) values('"+title+"','"+link+"','"+comment+"','"+price+"')"
            print(sql+'\n')
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 提交到数据库执行
                conn.commit()
                print("insert success\n")
            except:
                # 发生错误时回滚
                conn.rollback()
                os.system("pause")
                print("insert fail\n")
        conn.close()
        return item
