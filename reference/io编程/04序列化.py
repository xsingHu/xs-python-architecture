#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

unpickling pickling
"""

import pickle

d = dict(name='Bob', age=20, score=88)

print(pickle.dumps(d))

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# JSON
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换

import json

d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
j = json.dumps(d)
print(j)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
l = json.loads(json_str)
print(l)


# 对象 JSON
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str,object_hook=dict2student))












