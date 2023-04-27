class Master():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def pancake(self):
        print(f'{self.age}岁的{self.name}在摊煎饼')

class TuDi(Master):
    def kaolengmian(self):
        print(f'{self.age}岁的{self.name}在烤冷面')

class TuDi2(TuDi):
    pass


m = Master('老师傅',75)
m.pancake()
t = TuDi('张三',20)
t.pancake()
t.kaolengmian()

t2 = TuDi2('lisi',18)
t2.pancake()
t2.kaolengmian()
