# 例如，一起来完成：
# （1）定义一个存有HelloWorld的字符串变量；
data_1 = "HelloWorld"
# （2）获取变量中的H和W；
print(data_1[0],data_1[5])
# （3）获取变量的总长度；
print(len(data_1))
# （4）思考：如何获取变量的最后一个元素d。
print(data_1[len(data_1)-1])


# 例如，一起来完成：
# （1）定义一个字符串变量，内容为：HelloITHEIMA；
data_2 = "HelloITHEIMA"
# （2）截取索引值1到5之间的内容；
print(data_2[1:5])
# （3）截取索引值2到结尾的内容；
print(data_2[2:len(data_2)])
print(data_2[2:9999])
# （4）截取索引值2到倒数第2个的内容；
print(data_2[2:len(data_2)-1])
print(data_2[2:-1])
# （5）截取起始处到索引值为3的内容；
print(data_2[0:3])
# （6）截取索引1到8且每隔2个字母截取一下内容；
print(data_2[1:8:2])
# （7）截取索引2到10且每隔3个截取一下内容。
print(data_2[2:10:3])