# 无参无返回值的装饰器
def func1(f):
    def func2():
        print('正在计算中')
        f()

    return func2

@func1
def add():
    res = 10 + 20
    print(res)

add()




# 无参有返回值的装饰器
def func1_return(f):
    def func2():
        print('正在计算中')
        result = f()
        return result
    return func2


@func1_return
def add_return():
    res = 10 + 30
    return res


data = add_return()
print(data)


# 有参无返回值的装饰器