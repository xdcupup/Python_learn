# 例如，一起来完成：
# （1）一次长跑比赛中，体育老师说：本次长跑总共跑50圈，
# 如果有同学跑到第10圈时，感到身体不适，就直接退出比赛；
# （2）使用while循环和break模拟长跑效果。

# i = 1
# while True:
#     if i == 10:
#         print("end")
#         break
#     print(f"跑了{i}圈")
#     i+=1

for i in range(1,51):
    if i == 10:
        print("end")
        break
    print(f"跑了{i}圈")
