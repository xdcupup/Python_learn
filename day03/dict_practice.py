# 例如，一起来完成：
# （1）定义一个字典变量，存放一个学生的信息：姓名、性别、住址、年龄等；
data_dict = {'name':'张三','gender':'男','address':'中国','年龄':'18'}
# （2）输出并查看字典变量值与类型；
print(data_dict)
print(type(data_dict))
# （3）思考1：若给字典变量存放两个性别信息，会怎样？
# 有相同key值的数据只会保留一个，保留后面的key值数
data_dict2 = {'name':'张三','gender':'男','address':'中国','年龄':'18','gender':'女'}
print(data_dict2)
# （4）思考2：若给字典变量再存放一个薪酬，与年龄值相同，会怎样？
data_dict3 = {'name':'张三','gender':'男','address':'中国','年龄':'18','salary':'18'}
print(data_dict3)