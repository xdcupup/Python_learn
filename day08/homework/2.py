# 请使用装饰器方式来统计输出100000句"深圳黑马YYDS"的执行时间。
import time


def timer(f):
    def func1(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print(f'耗时:{end_time - start_time}秒')
        return res
    return func1

@timer
def func_str():
    for i in range(100000):
        print('深圳黑马YYDS')

func_str()

