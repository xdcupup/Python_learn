# 1. 创建一个动物(Animal)的基类，其中有一个run方法, 输出`跑起来....`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `吃东西...`
# 3. 创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马，同时针对吃东西，SwiftHorse类中重写eat方法，增加打印输出"`一天可以吃一担粮食...`"

class Animal():

    def run(self):
        print('跑起来')


class Horse(Animal):

    def eat(self):
        print('吃东西')


class SwiftHorse(Horse):

    def __init__(self,name):
        self.name = name

    def eat(self):
        super().eat()
        print('一天可以吃一担粮食...')

sh = SwiftHorse('千里马')
sh.eat()
sh.run()



