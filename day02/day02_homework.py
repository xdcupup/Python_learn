# 请通过用户输入姓名和当前年龄，若年龄超过64岁，提示：已到退休年龄，可以退休了；否则，提示：骚年好好加油，多多创造自身价值吧！
import decimal

# age = int(input("请输入年龄:"))
# if age > 64 :
#     print("已到退休年龄，可以退休了")
# else:
#     print("骚年好好加油，多多创造自身价值吧！")

# 在运输货物时，通常是：每吨货物每公里运费P(元)与运输距离S(运输公里数)有关，路途越远，每公里运价越低。
# 运输货物计算公式如下：
# | 每吨货物每公里运费P(元) | 运输距离S(运输公里数) |
# | :---------------------: | --------------------- |
# |           10            | s<100                 |
# |            8            | 100<=s<150            |
# |            7            | 150<=s<200            |
# |            6            | 200<=s<300            |
# |           5.5           | 300<=s<500            |
# |            5            | s>=500                |
# 还需注意的是，当所付的总运费超过5000元时，商家再给予九五折优惠。
# 请从键盘输入货物吨数、运输公里数，并使用代码求解应付的实际运费额。

# weight = decimal.Decimal(input("请输入货物吨数:"))
# mile = decimal.Decimal(input("请输入运输公里数:"))
# p0 = 0
# p = decimal.Decimal(p0)
# if mile > 0 and mile < 100:
#     p = 10
# elif mile >= 100 and mile < 150:
#     p = 8
# elif mile >= 150 and mile < 200:
#     p = 7
# elif mile >= 200 and mile < 300:
#     p = 6
# elif mile >= 300 and mile < 500:
#     p = 5.5
# elif mile >= 500:
#     p = 5
#
# total_fee_1 = decimal.Decimal(p) * decimal.Decimal(weight) * decimal.Decimal(mile)
# total_fee = decimal.Decimal(total_fee_1)
# if total_fee > 5000 :
#     total_fee = total_fee * decimal.Decimal(0.95)
# print(f"总费用为:{total_fee}")

# 制作用户登录系统：已知A用户注册的用户名为`heimauser`，密码是`123456`。要求如下：
# 		a.登录时需要验证用户名、密码、验证码(固定验证码为`ASDF`)；
# 		b.提示：系统先验证验证码是否正确，正确后再验证用户名和密码，试着使用if条件语句完成。

user_name = input("请输入用户名:")
password = input("请输入密码:")
verification_code = input("请输入验证码:")
if verification_code == "ASDF":
    if user_name == "heimauser" and password == "123456":
        print("登录成功!")
    else:
        print("用户名或密码错误!")
else:
    print("验证码错误!")


