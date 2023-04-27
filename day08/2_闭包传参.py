def func1(a, b):
    def func2(c, d):
        res = a + b + c + d
        return res
    return func2


f = func1(1,2)
data = f(3,4)
print(data)
