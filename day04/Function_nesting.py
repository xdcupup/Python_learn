# （1）先定义一个test()函数和func()函数；
# （2）接着，在函数test()中，嵌套调用func()函数，并在外部调用test()函数；
# （3）执行程序，观察效果；
# （4）思考：嵌套调用的执行流程是怎样的呢？

def test():
    print("调用test函数")
    func()

def func():
    print('调用func函数')

test()# 使用函数嵌套完成计算器的加减乘除