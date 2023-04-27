def func_1():
    a = '1'
    print(a)
func_1()


c ='123'
d=0

def func_2():
    global d
    d=c+'123'
func_2()
print(d)



def func_3():
    global c
    c = '1234'

func_3()
print(c)









# 变量的使用
# 局部变量  在函数内部定义的变量就是局部变量
def func():
    a = 10  # a就是局部变量
    print(a)


func()
# print(a)

# 全局变量  函数外部定义的变量，可以在函数内部使用
data = []


def func1():
    data.append({'name': '张三'})


func1()
print(data)


def func2():
    data.append({'name': '李四'})


func2()
print(data)


def func3():
    data.remove({'name': '张三'})


func3()
print(data)

# 等号赋值的方式修改全局变量
# = 赋值的方式修改全局变量需要通用global声明
def func4():
    data = (1,2,3,4)

func4()
print(data)