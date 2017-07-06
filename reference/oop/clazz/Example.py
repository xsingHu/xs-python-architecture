
class Example:
    def add(self):
        pass

    def _minus(self):
        pass

    def __multiply(self):
        pass


class A(object):
    pass

class B(A):
    pass

# isinstance() 是否是父类
# issubclass() 是否是子类

class Example2(object):

    @staticmethod
    def __new__(cls, *more):
        return super().__new__(cls, *more)

    def __init__(self,name,age):
        super().__init__()
        self.name = name
        self.age = age