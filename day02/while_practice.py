# 例如，一起来完成：
#
# （1）在生活中做事没让媳妇儿满意，跟她承认错误，说10遍：媳妇儿，我错了；
#
# data = 1
# while data < 10000 :
#     print("媳妇儿，我错了")
#     data = data + 1

# （2）可以使用哪些方式来完成呢？
#
# （3）思考：假定要说10000遍呢？该怎么办？


# 例如，一起来完成：
# （1）计算10 ~ 100之间所有自然数的和（包含10和100）；
# （2）分别使用正常和逆向思维来完成。
sum = 0
num = 10
while num < 100:
    sum = num + sum
    num += 1
    print(sum)