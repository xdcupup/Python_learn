# 例如，一起来完成：
import re
# （1）使用X*来匹配出一个字符串：第1个字母为大小写字母，后面都是小写字母且这些字母可有可无；
res = re.match('\w*','Itcast')
print(res)
# （2）通过X+来匹配一个具有数字、大小写字母、下划线的字符串；
res = re.match('\w+','Itcast123_')
print(res)
# （3）通过X?来匹配0到99之间的任意数字；
res = re.match('\d\d?','99')
print(res)
# （4）通过X{n,m}匹配出5到16位的密码，可以是大小写英文字母、数字、下划线。
res = re.match('\w{5}','123123123123')
print(res)
res = re.match('\w{5,16}','123XDc_')
print(res)