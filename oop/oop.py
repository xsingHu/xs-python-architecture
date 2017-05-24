
class Programer(object):
    hobby = 'Play Program'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @property
    def get_weight(self):
        return self.__weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    def  self_introduction(self):
        print("My Name is %s \nI am %s years old \n " % (self.name,self._age))

    def method(self,arg):
        pass

class BackendProgramer(Programer):

    def __init__(self,name,age,weight):
        super.__init__(name,age,weight)
        pass

    def method(self,arg):
        super(BackendProgramer,self).method(arg)
        # Programer.method(arg)  调用父类的方法
        pass


if __name__ == '__main__':
    programer = Programer('xsing',25,80)

    print(dir(programer))
    print(Programer.get_hobby()) # 静态

    print(programer.__dict__)

    # print(programer.get_weight())
    print(programer.get_weight)

    print(programer._Programer__weight) # __Programer_weight 可访问__weight

    print(programer.self_introduction())
    pass

