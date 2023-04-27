# 定义一个`Person` 类,包含初始化 init 方法:
# 实例属性:    名字, name
# 			  年龄, age
# 1. 记录由该类创建的对象的个数，创建一个对象，计数+1，删除一个对象，计数-1；
# 2. 定义一个方法，可以打印当前对象的个数；
# 3. 定义一个方法`show_info`, 输出以下信息
#    这是一个 Person 类,谢谢查看!
# 4. 打印对象的时候，可以输出打印自己的名字和年龄
#    我的名字是 xxx, 年龄是 xxx
# 5. 定义一个方法 `study`, 输出以下信息
#    我叫 xxx, 我要好好学习
# 6. 操作步骤
#    1.  调用`show_info `方法；
#    2.  创建两个对象, 打印当前对象，并打印当前的对象个数；
#    3.  分别使用两个对象调用`study`方法；
#    4.  删除一个对象，打印输出当前的对象个数。

class Person():
    # 初始化对象个数
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 对象个数加一
        Person.count += 1

    @classmethod
    def get_count(cls):
        print(f'{cls.count}个')
        # return cls.count


    def show_info(self):
        print('这是一个 Person 类,谢谢查看!')
        print(f'我的名字是{self.name}, 年龄是{self.age}')

    def study(self):
        print(f'我叫{self.name},我要好好学习')

# 对象个数减一
    def __del__(self):
        Person.count -= 1

p1 = Person('zhangsan',18)
p1.show_info()

p2  =Person('lisi',20)

# 打印当前的对象个数
Person.get_count()

p1.study()
p2.study()



