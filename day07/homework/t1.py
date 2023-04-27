# 1. 创建一个Animal（动物）基类，其中有一个run方法，输出`跑起来....`；
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run()方法还有eat()方法；
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `吃东西...`

class Animal():

    def run(self):
        print('跑起来')


class Horse(Animal):

    def eat(self):
        print('吃东西')




h = Horse()
h.run()
h.eat()
