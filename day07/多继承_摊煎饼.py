# 例如，一起来完成：
# （1）从前，有个摊煎饼的老师傅[Master]，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼技术；
# （2）渐渐地，老师傅老了，就想着把这套技术传授给他唯一的最得意的徒弟[TuDi]；
# （3）试着通过初始化、无参、定义方法与单继承来模拟程序。

class Master():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def pancake(self):
        print(f'{self.age}岁的{self.name}在摊煎饼')


class Master2():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def baozi(self):
        print(f'{self.age}岁的{self.name}在蒸包子')


class TuDi(Master,Master2):
    def kaolengmian(self):
        print(f'{self.age}岁的{self.name}在烤冷面')


m = Master('老师傅',75)
m.pancake()
m2 = Master2('大师傅',65)
m2.baozi()
t = TuDi('张三',20)
t.pancake()
t.kaolengmian()
t.baozi()
