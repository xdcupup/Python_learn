class Animal():
    def __init__(self,num,name):
        self.num = num
        self.name = name

    def eat(self):
        print(f'编号为{self.num}的{self.name}在吃饭')

    def sleep(self):
        print(f'编号为{self.num}的{self.name}在sleep')

    def jiao(self):
        pass
    def jiao_run(obj):
        obj.jiao()


class Dog(Animal):

    def jiao(self):
        print('wangwang')

class cat(Animal):

    def jiao(self):
        print('miaomiao')


d = Dog(1,'gou')
c = cat(2,'mao')
Animal.jiao_run(c)
Animal.jiao_run(d)

