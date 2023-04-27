# 求梯形面积

up = 10
low = 20
height = 30
acreage = (up + low) * height / 2
print(acreage)


# 提示用户输入圆的半径，用赋值运算符和公式S = πr^2，求圆的面积。

r = input("请输入半径:")
print(type(r))
r_int = int(r)
s = 3.14 * r_int ** 2
print("圆的面积为:",s)
