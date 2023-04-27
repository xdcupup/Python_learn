# def func_1(a,b,c):
#     res=a + b + c
#     print(res)
#
# func_1(1,2,3)
# func_1(b=2,c=3,a=1)


# 不定长参数
# 定义的时候不知道需要定义几个参数，就可以采用不定长参数
# *args  接受多个不同类型参数数据
# **kwargs  接受关键字的参数数据
def func3(*args):
    print(args)
    print(args[0])

# 调用
# 相同类型的多个数据
func3(1,2,3)
func3('1','2','3')
func3([1,2,3],[1,2,3])
# 不同类型
func3([1,2,3],'itcast')
# 关键字传递给*args  不支持
# func3(name='zhangsan')

def func4(**kwargs):
    print(kwargs)

func4(name='zhangsan',age=20)

# 终极参数接受方案
def func6(*args,**kwargs):
    print(args)
    print(kwargs)

func6('itcast',[1,2,3],name='zhangsan')