def func1():
    print('func1')


# 可以在函数内，通过参数调用另一个函数
def func3(f):
    # 参数当函数使用
    f()
    print('func3')


# 在调用时，将一个函数名当成参数进行传递
func3(func1)


# 匿名函数当成参数传递进行调用
def func4(f):
    res = f(10, 20)
    return res


res = func4(lambda a, b: a + b)
print(res)
