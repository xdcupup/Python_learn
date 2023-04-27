class obj1():
    def __init__(self):
        print('创建对象')

o = obj1()



class Car():

    def __init__(self):
        print('创建对象')
        self.wheel = 4
        self.color = 'red'

c = Car()
print(c.wheel)
print(c.color)



class Car2():

    def __init__(self,colour,wheel):
        print(wheel)
        print(colour)
c2 = Car2('red',4)


