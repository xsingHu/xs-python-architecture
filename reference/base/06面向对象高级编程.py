#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""



"""


class Student(object):
    pass


s = Student()
# 给实例绑定一个属性
s.name = 'zhangsan'
print(s.name)


# 给实例绑定一个方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(24)
print(s.age)


# 给所有实例都绑定方法,可以给class绑定方法

def set_score(self, score):
    self.score = score


Student.set_score = set_score
# 给class绑定方法后，所有实例均可调用
s.set_score(90)
print(s.score)

"""
使用__slots__
"""


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

# 使用@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

# Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self.birth = value

    @property
    def age(self):
        return 2015 - self._birth

# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# 多重继承
"""
通过多重继承，一个子类就可以同时获得多个父类的所有功能

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

"""


# 定制类
# __str__
class Student(object):

    def __init__(self,name):
        self.name = name

    def __str__(self) -> str:
        return 'this student name : %s' % self.name

    __repr__ = __str__

s = Student('zhangsan')

print(s)
# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in  Fib():
    print(n)

# __getitem__
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])

# __getattr__

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值

s = Student()
print(s.name)
print(s.score)
# print(s.age)

# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误

""""""
# __call__
"""
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
"""
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

"""
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

"""
print(callable(Student))
print(callable('str'))


# 枚举类
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数。

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique装饰器可以帮助我们检查保证没有重复值。

day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Tue'])

print(Weekday.Tue.value)

print(day1 == Weekday.Mon)

print(Weekday(1))

# print(Weekday(7))

# 使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。


def fn(self,name='hello'):
    print('hello ,%s.' %name)

Hello = type('Hello',(object,), dict(hello=fn))   # 创建Hello class

h = Hello()
h.hello()

"""
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
"""


# metaclass
"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
"""





























