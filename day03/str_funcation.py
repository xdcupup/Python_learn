# 例如，一起来完成：
# （1）定义一个字符串变量，内容有：  hello itheima big data    ；
str_1 = "  hello itheima big data    "
# （2）将变量中的空格替换为666；
print(str_1.replace(" ", "666"))
# （3）使用空格、字符a来分别分割字符串；
print(str_1.split(" "))
print(str_1.split("a"))
# （4）去掉字符串的前后空白内容。
print(str_1.strip())
print(str_1.strip(" "))


res_1 = str_1.strip().split(" ")
print(res_1)
