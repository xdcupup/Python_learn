# 例如，一起来完成：
import re
# （1）使用X|Y来匹配出0-100之间的所有数字字符结果；
res = re.match('(?P<a>\w+)@(?P<gongsi>\w+).com','123456@qq.com')
print(res)
print(res.group('a'))
print(res.group('gongsi'))
print(res.group(1))
print(res.group(2))
# （2）使用(X)来匹配出含有163、126、qq这几个内容且用户名位数为4-12位的邮箱，如itcast@163.com等。
res =re.match('(\w{4,12})@(163|126|qq).com','itcast@qq.com')
res2 =re.match('(\w{4,12})@(163|126|qq).com','itcas123123123123t@qq.com')
res3 =re.match('(\w{4,12})@(163|126|qq).com','itcast@gmail.com')
print(res)
print(res2)
print(res3)