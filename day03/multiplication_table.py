# 思考：例如，一起来完成：
# （1）使用嵌套循环来完成程序；
# （2）动手实践一个九九乘法表的显示效果。

for i in range(1,10):
#    print(' ')
    for j in range(1,i+1):
        res = i * j
        print(f"{i}*{j}={res}",end=" ")
    print(' ')