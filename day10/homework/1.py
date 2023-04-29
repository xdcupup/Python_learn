# 匹配出163或qq的邮箱地址，且@符号之前有4-20位，
# 例如itheima_hello@163.com、4008788909@qq.com。
import re

res = re.match('(\w{4,20})@(163|qq).com','itheima_hello@163.com')
print(res)
res = re.match('(\w{4,20})@(163|qq).com','4008788909@qq.com')
print(res)



# 请使用正则表达式来完成：
# （1）匹配100-1000之间的任意数；
res = re.match('1000|[1-9]\d\d','999')
print(res)
# （2）匹配出6到20位的用户昵称，可以是大小写英文字母、数字、下划线；
res = re.match('[a-z][A-Z][0-9][_]{6,20}','Aaa99_')
print(res)
# （3）匹配出QQ号，注意：QQ号全是数字，且当前位数有6位、7位、8位、9位、10位、11位；
res = re.match('\d{6,11}','1465952718')
print(res)
# （4）匹配任意字符；
res = re.match('\S+','12!@_aA')
print(res)
# （5）请提取字符串“黑马程序员官方客服400-618-9090,欢迎拨打!”中的联系方式。
res = re.match('(黑马程序员官方客服)(\d+)-(\d+)-(\d+),(欢迎拨打!)','黑马程序员官方客服400-618-9090,欢迎拨打!')
print(res.group(2,3,4))

