def func1():
    a = 100

    def func2():
        nonlocal a
        a = a+1
        print(a)
    return func2

f = func1()
f()