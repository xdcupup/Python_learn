data_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
res_str = ''
for i in range(6):
    index=random.randint(0,len(data_str)-1)
    index_str = data_str[index]
    res_str=res_str+index_str

print(res_str)