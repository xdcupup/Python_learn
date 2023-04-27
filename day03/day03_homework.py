# 对字符串"A10-20-30-40-50B"做处理，并获取出单个的数字值，且输出为int型的数字。

# data_str="A10-20-30-40-50B"
# str_b=data_str[1:15:1]
# str_c = print(str_b.split('-'))
#  for i in str_c:
#      print(i)






# 小张需要在一个字符串
# 'hello python'
# 中查找python这个关键字，如何实现？

data_str2 = 'hello python'
if "python" in data_str2:
    print('yes')
else:
    print("no")


# 编写代码模拟用户登录。要求：用户名为 python，密码 123456。
# ==给用户3次输入用户名和密码的机会==，如果3次中任意一次输入正确，打印“您已登录成功，欢迎光临”，程序结束；
# 如果3次都输入错误，则提示用户"您已3次输入用户名或密码有误, 登录失败~~"。
i=0
while i<3:
    user_name = input("请输入用户名:")
    password = input("请输入密码:")
    if user_name == "python" and password == "123456":
        print("您已登录成功，欢迎光临")
        break
    else:
        i+=1
print("您已3次输入用户名或密码有误, 登录失败~~")






