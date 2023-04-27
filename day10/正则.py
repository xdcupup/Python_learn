import re

data = input('请输入手机号:')

res = re.match('1\d{10}',data)

if res is None:
    print('wrong!')