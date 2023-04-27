# 例如，一起来完成：
# （1）小方同学当前`体重`是100kg；
# （2）每当他`跑步`一次时，则会减少0.5kg；
# （3）每当他`大吃大喝`一次时，则会增加2kg；
# （4）假如跑步5次后，再大吃大喝一次，体重如何？
# （5）请试着采用面向对象思想来编写案例。


class LoseWeight():
    weight = 100

    def run(self):
        self.weight = self.weight - 0.5


    def eat(self):
        self.weight = self.weight + 2

lw = LoseWeight()
for i in range(0,5):
    lw.run()
lw.eat()
print(lw.weight)
