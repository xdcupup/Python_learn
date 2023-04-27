# 定义一个有参数的函数，用于某人自我介绍，在该函数中需要完成用户的姓名、年龄、爱好等信息内容的输出。
def self_introduction(name, age, hobby):
    print(f"我叫{name},今年{age}岁,爱好是{hobby}")


self_introduction('张三', 18, '篮球')

# # 定义一个可以用于同时求解3个数的和与差的函数。
# def calculate_3():
#     equation = input('输入算式:')
#     if '+' in equation:
#         # 出现"+"时 说明是加法
#         arg_1 = equation.split('+')[0]
#         arg_2 = equation.split('+')[1]
#         arg_3 = equation.split('+')[2]
#         # 调用加法函数
#         res = add(arg_1,arg_2,arg_3)
#         print(f"结果为:{res}")
#     elif '-' in equation:
#         # 出现"-"时 说明是减法
#         arg_1 = equation.split('-')[0]
#         arg_2 = equation.split('-')[1]
#         arg_3 = equation.split('-')[2]
#         # 调用减法函数
#         res = subtractions(arg_1,arg_2,arg_3)
#         print(f"结果为:{res}")
# # 定义加法函数
# def add(a, b, c):
#     res = int(a) + int(b) + int(c)
#     return res
# # 定义加法函数
# def subtractions(a,b,c):
#     res = int(a) - int(b) - int(c)
#     return res
# # 调用主函数
# calculate_3()


products = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 178},
    {"name": "usb电动小风扇", "price": 59},
    {"name": "遮阳伞", "price": 36}
]
# 然后小明一共有8000块钱，那么他能不能买下这所有商品？如果能，请输出"能"，否则输出"钱不够，不能完成所有商品的购买"
object_0 = products[0]["price"]
object_1 = products[1]["price"]
object_2 = products[2]["price"]
object_3 = products[3]["price"]
total_price = object_0 + object_1 + object_2 + object_3
if total_price < 8000:
    print('能')
else:
    print("钱不够，不能完成所有商品的购买")


# 从键盘上输入年、月，通过return关键字来写一个函数，并返回当前月份的天数，
# 例如30、31等。【提示：`闰年就是能被4整除，且不能被100整除，或者能被400整除的年份。`】

def func_1():
    year_month = input("请输入年份和月份,用'-'隔开:")
    year = year_month.split('-')[0]
    month = year_month.split('-')[1]
    # print(year)
    # print(month)
    year = int(year)
    month = int(month)

    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 如果是闰年
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        month_list[1] = 29
        print(month_list[month - 1])
    else:
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(month_list[month-1])

    # if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #     return True
    # return False
x

func_1()
