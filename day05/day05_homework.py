# 从键盘上输入一个年份，用于验证是否是平年，若是平年，则输出"xxx年是平年。"；
# 若不是平年，则输出"---------->闰年！"，请使用函数的嵌套调用方式思考并分析问题。

def year_judgment():
    year = int(input('请输入年份:'))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year}年是闰年')
    else:
        print(f'{year}是平年.')


# year_judgment()


# 从键盘上输入一个5位数(数字)，判断它是不是回文数。所谓的回文数，指的是个位与万位相同、十位与千位相同的整数，例如：12321是回文数。
# （1）设计一个函数用来判断某个5位数是否为回文数；
# （2）提升程序的稳定性，可以对程序进行异常处理。
def palindromic_number_judgment():
    num = input('请输入一个五位的数字:')

    num_list = []
    for i in num:
        num_list.append(i)
    if num_list[4] == num_list[0] and num_list[3] == num_list[1]:
        print('回文数')
    else:
        print('不是回文数')


# palindromic_number_judgment()


# 请从键盘上输入年、月、日，并计算出该天是该年中的第几天。
# （1）提示：注意闰年、平年的情况；
# （2）可使用函数的嵌套调用分步骤完成。
def leap_common_year(year,month,day):
    num = 0
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    for m in range(1,month):
        if m in month_31:
            month_day = 31
        elif m == 2:
            month_day = 0
        else:
            month_day=30
        num+=month_day
        m=m-1

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            feb = 29
    else:
            feb = 28
    year_day = num+feb+day
    print(f'这一天是{year}年的第{year_day}天')

leap_common_year(2023,4,20)




