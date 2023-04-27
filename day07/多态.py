class Teacher():

    def __init__(self,name):
        self.name = name

    def run(self):
        print(f'{self.name}使用交通工具')

    def action_run(self):
        self.run()

class Car(Teacher):

    def __init__(self,type,name):
        self.type = type
        super().__init__(name)

    def run(self):
        print(f'{self.name}开{self.type}上班')

    def stop(self):
        print(f'{self.type}停止')

class Metro(Teacher):

    def __init__(self,line,name):
        self.line =line
        super().__init__(name)

    def run(self):
        print(f'{self.name}坐{self.line}号线上班')

    def stop(self):
        print(f'{self.name}号线到站')

c = Car('私家车','张三')
m  =Metro(3,'李四')


c.run()
c.stop()
m.run()
m.stop()


