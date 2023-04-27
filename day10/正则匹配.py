import re

res = re.match('.','.txt')
print(res)

res = re.match('...','E:\\itcast')
print(res)

res = re.match(r'E:\\','E:\\itcast')
print(res)

res=re.match(r'itcast','itcast')
print(res)