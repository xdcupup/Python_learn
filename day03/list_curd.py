# 增加
#例如，一起来完成：
#（1）定义一个列表变量，存放内容：中国、美国、英国、俄罗斯；
data_list = ["中国","美国","英国","俄罗斯"]
print(data_list)
#（2）在列表结尾处添加元素：德国；
data_list.append("德国")
print(data_list)
#（3）在元素美国后添加元素：日本；
data_list.insert(2,"日本")
print(data_list)
#（4）思考：若要在列表变量的结尾处，再新增元素：100、200、300，该怎么做？
data_list2 = [100,200,300]
data_list.extend(data_list2)
print(data_list)

data_list3 = data_list + data_list2
print(data_list3)

# 删除
# 例如，一起来完成：
#
# （1）定义一个列表变量，存放内容：中国、美国、英国、俄罗斯；
data_list4 = ["中国","美国","英国","俄罗斯"]
print(data_list4)
# （2）使用remove()删除元素：英国；
data_list4.remove("英国")
print(data_list4)
# （3）使用del删除元素：美国；
del data_list4[1]
print(data_list4)
# （4）执行程序，观察效果。


# 修改
# （1）定义一个列表变量，存放内容：中国、美国、英国、俄罗斯；
data_list5 = ["中国","美国","英国","俄罗斯"]
print(data_list5)
# （2）将中国修改为中华人民共和国；
data_list5[0] = '中华人民共和国'
print(data_list5)
# （3）修改俄罗斯为Russia；
data_list5[3] = 'Russia'
print(data_list5)
# （4）执行程序，观察效果。


# 查找
# 例如，一起来完成：
# （1）因["192.168.1.15", "10.1.1.100", "172.35.46.128","172.32.24.99"]等IP地址存在恶意访问黑马程序员官网，被列为访问黑名单；
data_list6 = ["192.168.1.15", "10.1.1.100", "172.35.46.128","172.32.24.99"]
# （2）获取黑名单IP列表的长度；

# print(len(data_list6))
# # （3）从键盘上输入一个IP地址，并用于判断是否是黑名单IP地址？
# ip = input("ip:")
# if ip in data_list6:
#     print("yes")
# else:
#     print("no")


my_list = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(my_list[0])
print(my_list[1])
print(my_list[1][0])
print(my_list[1][1][0])

list_123 = [{'a':'1','b':'2','c':'3'},{'d':'4','e':'5','f':'6'},{'g':'7','h':'8','i':'9'}]
print(list_123[0])
print(list_123[0]['a'])
print(list_123[1]['d'])
print(list_123[2]['g'])
