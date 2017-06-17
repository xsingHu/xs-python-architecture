class Programer(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other,Programer):
            return self.age == other.age
        raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other,Programer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programer')

#      运算符: 魔术方法处理运算符逻辑
if __name__ == '__main__':
    p1 = Programer("hello",25)
    p2 = Programer('world',30)
    print(p1==p2)
    print(p1+p2)

# 类的展现
# __str__
# __repr__
# __unicode__
    # eval

# __dir__  dir()

# __setattr__ 设置对象属性
# __getattr__ 查询对象属性
# __getattribute__
# __delattr__
