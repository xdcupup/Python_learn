# 例如，一起来完成：
# （1）定义一个列表变量1，用于存放几个知名大学名称；
list_1 = ['北京大学','清华大学','上海大学']
print(list_1)
# （2）定义一个列表变量2，用于存放某学生的姓名、年龄、存款、是否男生等信息；
list_2 = ['张三',18,100.45,'男']
print(list_2)
list_3= [['张三',18,100.45,'男'],['李四',23,99.99,'男']]
print(list_3)
# （3）思考：要把字符串Python转换为列表list类型的值，该怎么做？
# 使用 append 方法
list_4   = []
print(list_4)
for i in 'itcast':
    list_4.append(i)
print(list_4)

# split方法切割的数据存入到列表中
data = 'itcast'
list_5 = data.split()
print(list_5)



# 例如，一起来完成：
# （1）获取知名大学名称列表变量的元素总个数；
len(list_1)
print(len(list_1))
# （2）获取列表变量的第1个和第3个位置对应的元素值；
print(list_1[0])
print(list_1[2])
# （3）思考：若直接访问不存在的第100个元素值，会怎样？

print(list_1[1:2])
print(list_1[1:100])