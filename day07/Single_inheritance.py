class Master():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pancake(self):
        print(f'{self.age}岁的{self.name}在摊煎饼')


class TuDi(Master):

    def hand_grasping_cake(self):
        print(f'{self.age}岁的{self.name}在做手抓饼')


m = Master('zhangsan',30)
m.pancake()

t = TuDi('lisi',40)
t.pancake()
t.hand_grasping_cake()
