# 例如，一起来完成：
# （1）通过int()将键盘输入的幸运数字，转换为整型结果；

# lucky_num =int(input("请输入幸运数字:"))
# print(lucky_num +10)

#  拓展 ：（3）改进：如何解决超市收银系统的计算价格有误的问题？
# 将数据转化为decimal类型后在进行加减乘除计算

import decimal
data_dec = decimal.Decimal(3.1415926)
print(type(data_dec))
print(data_dec)
# 对decimal类型的数据指定保留的小数位数
data_dec2 =data_dec.quantize(decimal.Decimal('0.0000'))
print(data_dec2)





