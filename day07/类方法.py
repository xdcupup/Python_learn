# 例如，一起来完成：
# （1）定义一个小狗类，且小狗很喜欢吃骨头；[类方法]
# （2）仔细观察，小狗有属于自己独有的犬牙；[类属性]
# （3）思考：若要从外部访问小狗的犬牙，该怎么做呢？

class Dog():
    tooth = '犬牙'

    def func(self):
        print('对象方法')

    @classmethod
    def func_cls(cls):
        print('吃骨头')
        print(cls.tooth)
        print(cls.__name__)

    @staticmethod
    def func_static():
        print('1')
        print('2')
        print('3')
        print('4')


    @property
    def func_attr(self):
        print('func_attr方法')

# 创建对象
d = Dog()



d.func()
# Dog.func()

d.func_cls()
Dog.func_cls()

d.func_static()
Dog.func_static()