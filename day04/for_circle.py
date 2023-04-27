# 例如，一起来完成：
# （1）定义一个字典变量，存放一个学生的信息：姓名、住址、年龄等；
# （2）获取字典变量中的所有键，观察效果；
# （3）思考：若要输出【键 --> 值】形式结果，该怎么做？

data_dict={}

data_dict['name']='张三'
print(data_dict)

key ='age'
value=18
data_dict[key] = value
print(data_dict)
# 修改字典数据
# 如果key存在是修改数据 ，如果key不存在则增加数据
data_dict['name'] = '李四'
print(data_dict)

# 删除字典
del data_dict['name']
print(data_dict)

# 查询字典
data = data_dict.get('age')
print(data)
data1 = data_dict.get('name','itcast')
print(data1)
print(data_dict)


# 添加数据
data_dict['name']  = '李四'


#字典循环遍历
print('-------------字典遍历-------------')
print(data_dict)
# for循环时会取出key
for k in data_dict:
    print(k)
for k in data_dict.keys():
    print(k)

# for循环取value值
for v in data_dict.values():
    print(v)

# for 循环同时取k和v
for k,v in data_dict.items():
    print(f'key:{k},value:{v}')
