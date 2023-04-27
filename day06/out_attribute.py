# （1）在车类外设置车的颜色为红色、有4个轮胎；
# （2）获取属性值并输出结果。

class Car():
    wheel = 0
    colour = ''

    def car_show(self):
        print(f'车的颜色是{self.colour}有{self.wheel}个轮子')


c = Car()
c.wheel = 4
c.colour = '红色'

c.car_show()