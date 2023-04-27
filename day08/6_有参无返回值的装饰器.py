# 有参无返回值的装饰器
def func_1args(f):
    def func2(a,b):
        print('正在计算中')
        f(a,b)
    return func2

@func_1args
def func_add(a,b):
    res = a + b
    print(res)

func_add(1,2)



