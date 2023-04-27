def comment():
    print('实现评论功能')

def buy():
    print('实现购买功能')



def func1(f):
    def func2():
        print('装饰器实现登录')
        f()
    return func2

f = func1(comment)
f()

f = func1(buy)
f()