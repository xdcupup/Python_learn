# 无参无返回值
def outer1(f):
    def func1():
        print('123')
        f()

    return func1


@outer1
def add_1():
    res = 1 + 2
    print(res)


add_1()

print('---' * 100)


# 无参有返回值
def outer2(f):
    def func2():
        print('123')
        res1 = f()
        return res1

    return func2


@outer2
def add_2():
    res = 1 + 2
    return res


data = add_2()
print(data)

print('---' * 100)


# 有参有返回值
def outer3(f):
    def func3(a, b):
        print('123')
        res5 = f(a, b)
        return res5

    return func3


@outer3
def add4(a, b):
    res2 = a + b
    return res2


data2 = add4(5, 6)
print(data2)

print('---' * 100)


def fun_out(a):
    print(a)
    def universal_decorator(f):
        def func7(*args,**kwargs):
            print('增加的业务功能')
            res = f(*args,**kwargs)
            return res
        return func7
    return universal_decorator

@fun_out('789')
# @universal_decorator
def add_5(a,b):
    res = a+b
    return res

data3 = add_5(9,9)
print(data3)



