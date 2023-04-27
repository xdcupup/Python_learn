# 1. 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中重写run方法，增加打印输出"`迈着矫健的步伐跑起来!!`"，同时实现eat方法, 输出 `吃东西...`

class Animal():

    def run(self):
        print('跑起来')

class Horse(Animal):

    def run(self):
        super().run()
        print('迈着矫健的步伐跑起来!!')

    def eat(self):
        print('吃东西')

h=Horse()
h.run()
h.eat()
