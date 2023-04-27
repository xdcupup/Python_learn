# 父类方法调用
class Master():
    def __init__(self, name, age):
        # 创建对象时传递数据
        self.name = name
        self.age = age

    def func(self):
        print(f'{self.age}的{self.name}在摊煎饼')

# 创建对象
m = Master('师傅',40)
m.func()

class Master2():
    def __init__(self, name, age):
        # 创建对象时传递数据
        self.name = name
        self.age = age

    def func(self):
        print(f'{self.age}的{self.name}在包子')

# 继承方式，获取所有老师傅的技能
class TuDi(Master,Master2):
    # 继承的Master中有func

    def func(self):
        # 定义了和父类相同的方法，相当于对原来的方法进行重写，在执行时按照新的逻辑执行
        print('徒弟中的func方法')
        # 调用父类中func
        super().func()  # 当有多个父类时，按照执行顺序先执行第一个类

    def func2(self):
        print(f'{self.age}的{self.name}在做手抓饼')

t = TuDi('徒弟',20)
t.func()
t.func2()