class Animal():
    def __init__(self,num,name):
        self.num = num
        self.name = name

    def eat(self):
        print(f'编号为{self.num}的{self.name}在吃饭')

    def sleep(self):
        print(f'编号为{self.num}的{self.name}在sleep')

class Dog(Animal):

    def jiao(self):
        print('wangwang')

class cat(Animal):

    def jiao(self):
        print('miaomiao')


d = Dog(1,'gou')
d.eat()
d.sleep()
d.jiao()

c = cat(2,'mao')
c.eat()
c.jiao()
c.sleep()