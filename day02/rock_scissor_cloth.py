import random
# （1）显示操作界面：石头1  剪刀2  布3
# （2）玩家出拳；
# （3）电脑要出拳；
# （4）判断玩家
# 	胜利：玩家1  电脑2；  玩家2  电脑3；  玩家3  电脑1；
# 	平局：玩家1  电脑1；  玩家2  电脑2；  玩家3  电脑3；
# 	失败：另外的。
while True:
    print("石头1  剪刀2  布3")
    player = int(input("请出拳:"))
    com = random.randint(1,3)
    if com == 1:
        print("电脑出石头")
    elif com == 2:
        print("电脑出剪刀")
    elif com == 3:
        print("电脑出布")

    if player == com :
        print("平局")
    elif player == 1 and com == 2 or player == 2 and com == 3 or player == 3 and com == 1 :
        print("胜利")
    else:
        print("失败")
