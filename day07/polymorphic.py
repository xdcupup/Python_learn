# 多态实现
class Teacher():

    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'{self.name}使用交通工具')

    def action_run(self):
        self.run()


class Car(Teacher):

    def __init__(self, type, name):
        self.type = type
        super().__init__(name)

    def run(self):
        print(f'{self.name}开{self.type}上班')

    def stop(self):
        print(f'{self.type}停止')


class Metro(Teacher):
    # 定义地铁类
    def __init__(self, line, name):
        self.line = line
        super().__init__(name)

    def run(self):
        print(f'{self.name}坐地铁{self.line}线上班')

    def stop(self):
        print('地铁停车到站')


c = Car('小轿车', '张三')
m = Metro(8, '张三')

Teacher.action_run(m)
