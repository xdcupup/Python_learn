# 一个函数, 返回一个字符串, 使用装饰器实现对这个字符串添加后缀.txt。

def str_add(f):
    def func1(*args, **kwargs):

        res = f()+'.txt'
        return res
    return func1

@str_add
def str():
    str_1 = '123'
    return str_1

data = str()
print(data)






