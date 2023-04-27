def func1_args_return(f):
    def func1(a,b):
        print('正在计算中')
        res= f(a,b)
        return res
    return  func1

@func1_args_return
def func_add(a,b):
    res = a+ b
    return res

data = func_add(1,2)
print(data)