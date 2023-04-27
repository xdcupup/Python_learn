# 多层继承
class Master():
    def __init__(self, name, age):
        # 创建对象时传递数据
        self.name = name
        self.age = age

    def func(self):
        print(f'{self.age}的{self.name}在摊煎饼')

# 创建对象
# m = Master('师傅',40)
# m.func()

# 继承方式，获取老师傅的技能
class TuDi(Master):

    def func(self):
        print(f'{self.age}的{self.name}在做手抓饼')

# t = TuDi('徒弟',20)
# t.func()

class  TuDi2(TuDi):
    pass


t2 = TuDi2('徒弟的徒弟',18)
t2.func()

print(TuDi2.mro())
