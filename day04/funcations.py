# 例如，一起来完成：
# 对容器类型数据的公共方法使用
# + 号合并数据
data_str1 = 'itcast'
data_str2 = 'itheima'
data_list1 = ['a', 'c', 'b']
data_list2 = ['d', 'f', 'g']
data_dict1 = {'name': 'zhangsan', 'age': 20}
data_dict2 = {'name': 'lisi', 'age': 22}
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = (5, 6, 7, 8)
data_set1 = {1, 2, 3, 4}
data_set2 = {5, 6, 7, 8}


res_data1 = data_str1 + ',' + data_str2
print(res_data1)

res_data2=data_list1+data_list2
print(res_data2)

# 字典数据不支持+
# res_data3 =data_dict1+data_dict2
# print(res_data3)

res_data4=data_tuple1+data_tuple2
print(res_data4)

# set集合数据不支持+合并
# res_data5 = data_set1 + data_set2
# print(res_data5)



# *  复制
res_data6 = data_str1*10
print(res_data6)

res_data7=data_list1*10
print(res_data7)

#字典不支持复制
# res_data8 = data_dict1 * 10
# print(res_data8)

# 判断元素是否在字符串，列表字典集合中
print('i' in data_str1)
print('i' in data_list1)
print('name' in data_dict1)  # 判断key是否存在  不能判断value是否存在
print(8 in data_tuple2)
print(10 in data_set1)
