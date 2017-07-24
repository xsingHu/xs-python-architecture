#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
"""
  uri = "mongodb://%s:%s@%s" % (
                quote_plus(user), quote_plus(password), host)
            client = MongoClient(uri)
"""
c = MongoClient()
# 选择操作的数据库
db = c.test
# 选择操作的集合
collection = db.person
# 定义集合
item = {
    "name":"张三",
    "age":18
}
# 插入集合
collection.insert(item)
# 查找集合
print(str(collection.find_one()))



