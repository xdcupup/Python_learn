# 新增
# 例如，一起来完成：
# （1）定义一个字典变量，存放老师信息：姓名、体重、年龄等；
curd_dict = {'name':'张三','weight':'180','age':'40'}
print(curd_dict)
# （2）给老师变量添加一个兴趣爱好；
curd_dict['hobby']='跳舞'
print(curd_dict)
# （3）思考：若给一个空字典添加2个元素，该怎么做？
curd_dict2 = {}
print(curd_dict2)
curd_dict2['a'] = '1'
curd_dict2['b'] = '2'
print(curd_dict2)
# （4）执行程序，观察效果。

# 删除
# 例如，一起来完成：
# （1）定义一个字典变量，存放老师信息：姓名、体重、年龄等；
curd_dict3 = {'name':'张三','weight':'180','age':'40'}
print(curd_dict3)
# （2）试着删除字典的体重元素；
del curd_dict3['weight']
print(curd_dict3)
# （3）思考：当要给字典变量重新添加数据时，该怎么办？
curd_dict3['name'] = '张三'
curd_dict3['weight'] = 180
print(curd_dict3)

# 修改
# 例如，一起来完成：
# （1）定义一个字典变量，存放老师信息：姓名、体重、年龄等；
curd_dict4 = {'name':'张三','weight':'180','age':'40'}
print(curd_dict4)
# （2）修改字典变量的姓名、体重值。
curd_dict4['name']='李四'
curd_dict4['weight'] = '150'
print(curd_dict4)


# 查找
# 例如，一起来完成：
# （1）定义一个字典变量，存放老师信息：姓名、体重、年龄等；
# （2）使用两种方式来查看老师的姓名、年龄。
curd_dict5 = {'name':'张三','weight':'180','age':'40'}
print(curd_dict5['name'])
print(curd_dict5.get('name'))






