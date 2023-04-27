# （1）地瓜被烤`时间`、`生熟程度`是有关联的；
# （2）用户可以按照自己意愿添加`调料`；
# （3）当持续烤地瓜后，观察烤地瓜的效果。
# 被烤时间、生熟程度的关联：
# 0-5分钟：生的
# 5-15分钟：半生不熟
# 15-25分钟：熟了
# 超过25分钟：已烤焦，糊了
# `添加调料`操作：
# 添加的调料：用户可以按自己的意愿添加调料。

class SweetPotato():
    degree_of_cooking = ''
    season = []

    # degree_of_cooking = ['raw','halfcooked','cooked','overcooked']
    # seasoning = ['salt','sugar']

    def bake_time(self, b_time):
        if b_time >= 0 and b_time <= 5:
            self.degree_of_cooking = 'raw'
            print(f'烤了{b_time}分钟,{self.degree_of_cooking}了')
        elif b_time > 5 and b_time <= 15:
            self.degree_of_cooking = 'halfcooked'
            print(f'烤了{b_time}分钟,{self.degree_of_cooking}了')
        elif b_time > 15 and b_time <= 25:
            self.degree_of_cooking = 'cooked'
            print(f'烤了{b_time}分钟,{self.degree_of_cooking}了')
        elif b_time > 25:
            self.degree_of_cooking = 'overcooked'
            print(f'烤了{b_time}分钟,{self.degree_of_cooking}了')

    def seasoning(self, s):
        self.season.append(s)
        print(f"加了{self.season}")

potato = SweetPotato()

potato.bake_time(20)
potato.seasoning('salt')
potato.seasoning('sugar')
print(potato)


