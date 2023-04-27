def UniversalDecorator(f):
    def func1(*args, **kwargs):
        print('增加的业务功能')
        res = f(*args, **kwargs)
        return res

    return func1

@UniversalDecorator
def func_add():
    res = 1+2
    print(res)

func_add()



@UniversalDecorator
def func_add1():
    res = 1 + 2
    return res

print(func_add1())


@UniversalDecorator
def func2_add(a,b):
    res  = a+b
    print(res)

func2_add(2,2)


@UniversalDecorator
def func_add3(a,b):
    res =a+b
    return res

data = func_add3(3,3)
print(data)