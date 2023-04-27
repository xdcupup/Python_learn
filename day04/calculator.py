# 使用函数嵌套完成计算器的加减乘除
# 定义计算器的主函数 calculator_func
def calculator_func():
    print('欢迎使用计算器!')
    equation = input('请输入要计算的公式:')


    if '+' in equation:
        # 出现"+"时 说明是加法
        arg_1 = equation.split('+')[0]
        arg_2 = equation.split('+')[1]
        # 调用加法函数
        res = add(arg_1, arg_2)
        print(f'结果为:{res}')

    elif '-' in equation:
        # 出现"-"时 说明是减法
        arg_1 = equation.split('-')[0]
        arg_2 = equation.split('-')[1]
        # 调用减法函数
        res = subtractions(arg_1, arg_2)
        print(f'结果为:{res}')

    elif '*' in equation:
        # 出现"*"时 说明是乘法
        arg_1 = equation.split('*')[0]
        arg_2 = equation.split('*')[1]
        # 调用乘法函数
        res = plus(arg_1, arg_2)
        print(f'结果为:{res}')

    elif '/' in equation:
        # 出现"/"时 说明是除法
        arg_1 = equation.split('/')[0]
        arg_2 = equation.split('/')[1]
        # 调用除法函数
        res = division(arg_1, arg_2)
        print(f'结果为:{res}')
# 定义加法函数
def add(a,b):
    res = int(a) + int(b)
    return res
# 定义减法函数
def subtractions(a,b):
    res = int(a) - int(b)
    return res
# 定义乘法函数
def plus(a,b):
    res = int(a) * int(b)
    return res
# 定义除法函数
def division(a,b):
    res = int(a) / int(b)
    return res


while True:
    # 调用主函数
    calculator_func()
    data=input("要继续吗?   输入1结束 任意键继续")
    if data == '1':
        break