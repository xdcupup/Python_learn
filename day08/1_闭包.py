def func1():
    a = 10

    def fun2():
        res = a + 10
        print(res)

    return fun2


f = func1()
f()



