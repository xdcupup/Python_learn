# 定义小数price、weight、money，输出`苹果单价9.00元／⽄，购买了5.00⽄，需要支付45.00元`。[备注：记得添加必要的注释。]
# 定义小数price、weight、money，
price = 9.00
weight = 5.00
money = price * weight
# 输出`苹果单价9.00元／⽄，购买了5.00⽄，需要支付45.00元`
print(f"苹果单价{price}元／⽄，购买了{weight}⽄，需要支付{money}元")
print("苹果单价%.2f元／⽄，购买了%.2f⽄，需要支付%.2f元" %(price,weight,money))


"""
用户登录系统：用户输入用户名和密码，在控制台格式化输出用户输入的用户名和密码。[备注：记得规范化变量命名。]效果如下：

>   请输入用户名：Jerry
>   请输入密码：jerry666
>   您好，您输入的用户名是Jerry, 密码是jerry666，欢迎登录系统。
"""

#user_name = input("请输入用户名:")
#password = input("请输入密码:")

#print(f"您好，您输入的用户名是{user_name}, 密码是{password}，欢迎登录系统。")



# 已知用户姓名、年龄、体重数据，要求从键盘上录入用户信息，并在控制台格式化输出用户信息，
# 例如`用户姓名:TOM,年龄:18岁,当前体重是50.55kg。`。[备注：记得规范化变量命名，以及添加必要的注释。]

# user_name01 = input("请输入姓名:")
# age = input("请输入您的年龄:")
# body_weight = input("请输入您的体重:")
# print(f"用户姓名:{user_name01},年龄:{age}岁,当前体重是{body_weight}kg。")


#  定义⼀个小数scale=10，输出`数据比例是10.00%`。
scale = float(10)

print(f"数据比例是{scale}%")
print("数据比例是%.2f%%" %scale)